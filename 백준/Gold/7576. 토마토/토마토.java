import java.util.*;
import java.io.*;

class Main{
    static int M, N;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static boolean canGo(int i, int j){
        return i>=0 && i<N && j>=0 && j<M ? true : false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        int INF = Integer.MAX_VALUE;

        int[][] tomatoes = new int[N][M];
        int[][] visited = new int[N][M];

        Queue<int[]> q = new LinkedList<>();

        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++){
                int temp = Integer.parseInt(st.nextToken());
                if (temp == 1){
                    q.add(new int[]{i, j});
                    visited[i][j] = 0;
                } else if (temp == -1){
                    visited[i][j] = -1;
                } else {
                    visited[i][j] = INF;
                }
            }
        }

        while (!q.isEmpty()){
            int[] cur = q.poll();
//            System.out.println(cur[0] + ", "+ cur[1]);
            for (int i = 0; i<4; i++) {
                int[] next = new int[]{cur[0] + dx[i], cur[1] + dy[i]};
//                System.out.println(next[0] + ", "+ next[1]);
                if (canGo(next[0], next[1])) {
                    if (visited[next[0]][next[1]] == INF){
                        visited[next[0]][next[1]] = visited[cur[0]][cur[1]] + 1;
                        q.add(new int[]{next[0], next[1]});
                    }
                }
            }
        }

//        System.out.println(Arrays.toString(visited[0]));

        int answer = 0;

        for (int i = 0; i < N; i++){
            for (int j = 0; j < M; j++){
                answer = Math.max(answer, visited[i][j]);
            }
        }

        System.out.println(answer!=INF?answer:-1);
    }
}
