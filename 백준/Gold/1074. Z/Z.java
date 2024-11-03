
import java.util.*;
import java.io.*;

class Main{
    static int N, r, c;
    static int answer;

    static void find(int i, int j, int len, int cnt){
//        System.out.println(i+", "+j+", "+len + ", "+ cnt);

        if (len == 1){
            answer = cnt;
            return;
        }

        if (r < i + len/2){
            if (c <  j + len/2){
                find(i, j, len/2, cnt);
            } else {
                find(i, j + len/2, len/2, cnt + (int)Math.pow(len/2, 2));
            }
        } else {
            if (c <  j + len/2){
                find(i + len/2, j, len/2, cnt+2*(int)Math.pow(len/2, 2));
            } else {
                find(i + len/2, j + len/2, len/2, cnt + 3*(int)Math.pow(len/2, 2));
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        int size = (int) Math.pow(2, N);

        find(0, 0, size, 0);

        System.out.println(answer);

    }
}