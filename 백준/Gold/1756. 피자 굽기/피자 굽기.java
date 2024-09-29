/**
 * N개의 피자 반죽을 구우려고 함
 * 오븐이 깊은 관처럼 생겼는데 지름이 깊이에 따라 변함
 * 피자 반죽은 완성 순서대로 오븐에 들어감
 * 맨 위의 피자가 얼마나 깊이 들어갔는지 알아내기
 */
import java.io.*;
import java.util.*;


public class Main {
    int D, N;
    int[] oven, pizza;
    int answer = 0;
    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        D = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        oven = new int[D];
        pizza = new int[N];

        int temp;
        oven[0] = Integer.parseInt(st.nextToken());
        for (int i = 1; i < D; i++){
            temp = Integer.parseInt(st.nextToken());
            if (oven[i-1] < temp){
                oven[i] = oven[i-1];
            }else{
                oven[i] = temp;
            }
        }

        st = new StringTokenizer(br.readLine());

        for (int j = 0; j < N; j++){
            pizza[j] = Integer.parseInt(st.nextToken());
        }

        int oi = D-1;
        int pi = 0;

        while (pi < N && oi >= 0){
//            System.out.println("oi = " + oi);
//            System.out.println("pi = " + pi);
            if (oven[oi] < pizza[pi]){
                oi -= 1;
            } else{
                pi += 1;
                oi -= 1;
            }
        }

        if (pi >= N){
            answer = oi +2;
        }
        System.out.println(answer);

    }

    public static void main(String args[]) throws Exception {
        new Main().solution();
    }
}
