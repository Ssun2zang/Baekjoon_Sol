/**
 * 비에 안 잠기는 안전 구역 개수 세기
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    int N;
    int[][] map;
    boolean[][] visited;
    int minVal = Integer.MAX_VALUE, maxVal, answer;
    int[] dx = {1, -1, 0, 0};
    int[] dy = {0, 0, 1, -1};

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        map = new int[N][N];

        int val;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                val =  Integer.parseInt(st.nextToken());
                if (val > maxVal) maxVal = val;
                else if (val < minVal) minVal = val;
                map[i][j] = val;
            }
        }

        int safety = 0;

        if (minVal == maxVal){
            System.out.println(1);
            return;
        }

        for (int i = minVal; i < maxVal; i++){
            // 찾는 로직
            visited = new boolean[N][N];
            safety = search(i);

            if (answer < safety) answer = safety;
        }

        System.out.println(answer);
    }

    public int search(int threshold){

        int temp = 0;
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                // 안전 구역
                if (visited[i][j]){
                    continue;
                }

                if (map[i][j] > threshold){
                    temp += 1;
                    bfs(i, j, threshold);
                }

            }
        }

        return temp;
    }

    public void bfs(int curX, int curY, int thr){
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{curX, curY});
        visited[curX][curY] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int i = cur[0], j = cur[1];

            for (int k = 0; k < 4; k++) {
                int a = i + dx[k], b = j + dy[k];
                if (a < 0 || a >= N || b < 0 || b >= N) {
                    continue;
                }

                if (visited[a][b]) {
                    continue;
                }

                visited[a][b] = true;

                if (map[a][b] > thr) {
                    q.offer(new int[]{a, b});
                }


            }
        }
    }

    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}
