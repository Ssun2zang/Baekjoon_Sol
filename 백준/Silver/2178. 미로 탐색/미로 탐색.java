import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import java.util.LinkedList;
import java.util.Queue;


public class Main {
    int N, M;
    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int INF = Integer.MAX_VALUE;
        char[][] maze;
        int[][] visited;
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        int answer = 0;

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        maze = new char[N][M];
        visited = new int[N][M];

        for (int i = 0; i < N; i ++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++){
                maze[i][j] = line.charAt(j);
                visited[i][j] = INF;
            }
        }



        Queue<int[]> q = new LinkedList<>();
        int[] cur = {0, 0};
        visited[cur[0]][cur[1]] = 1;
        q.offer(cur);

        while(!q.isEmpty()){
            cur = q.poll();
            int curX = cur[0];
            int curY = cur[1];

            for(int i = 0; i < 4; i ++){
                int nextX = curX + dx[i];
                int nextY = curY + dy[i];
//                System.out.printf("%d %d\n",nextX, nextY);

                if (nextX<0 || nextX>=N || nextY<0 || nextY>=M){
                    continue;
                }

                if (maze[nextX][nextY]=='0' || visited[nextX][nextY]!= INF){
                    continue;
                }

                if (nextX == N-1 && nextY == M-1){
                    System.out.println(visited[curX][curY] + 1);
                    return;
                }

                visited[nextX][nextY] = visited[curX][curY] + 1;
                q.offer(new int[]{nextX, nextY});

            }
        }

        System.out.println(visited[N-1][M-1]);

    }

    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}