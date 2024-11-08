import java.io.*;
import java.util.*;

/**
 * 양이 늑대보다 많으면 늑대를 다 잡아먹음
 * . 빈공간, # 울타리, 늑데 v, 양 k
 * 양과 늑대 몇 마리가 살아남을지 계산하기
 * 살아남는 양과 늑대의 수를 각각 출력하기
 */
public class Main {
    static int R, C;
    static char[][] map;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new char[R][C];
        boolean[][] visited = new boolean[R][C];

        for (int i = 0; i<R; i++){
            String str = br.readLine();
            for (int j = 0; j<C; j++){
                map[i][j] = str.charAt(j);
            }
        }
        int sh = 0;
        int wo = 0;
        int[] dx = new int[]{1, -1, 0, 0};
        int[] dy = new int[]{0, 0, 1, -1};

        for (int i = 0; i<R; i++){
            for (int j = 0; j<C; j++){
                if (visited[i][j]) {
                    continue;
                }
                Queue<int[]> q = new LinkedList<>();
                q.add(new int[]{i, j});
                visited[i][j] = true;
                int sh_temp = 0;
                int wo_temp = 0;
                if (map[i][j]=='v'){
                    wo_temp++;
                } else if (map[i][j]=='k'){
                    sh_temp++;
                }

                while (!q.isEmpty()) {
                    int[] cur = q.poll();
                    for (int k = 0; k < 4; k++) {
                        int nextX = cur[0] + dx[k];
                        int nextY = cur[1] + dy[k];

                        if (nextX >= 0 && nextX < R && nextY >= 0 && nextY < C) {
                            if (!visited[nextX][nextY]) {
                                visited[nextX][nextY] = true;
                                if (map[nextX][nextY]=='v'){
                                    wo_temp++;
                                } else if (map[nextX][nextY]=='k'){
                                    sh_temp++;
                                }

                                if (map[nextX][nextY] != '#') {
                                    q.add(new int[]{nextX, nextY});
                                }
                            }
                        }
                    }
                }
//                System.out.println("wo_temp = " + wo_temp);
//                System.out.println("sh_temp = " + sh_temp);

                if (sh_temp > wo_temp){
                    sh += sh_temp;
                } else{
                    wo += wo_temp;
                }
            }
        }

        System.out.println(sh+ " "+ wo);
    }
}
