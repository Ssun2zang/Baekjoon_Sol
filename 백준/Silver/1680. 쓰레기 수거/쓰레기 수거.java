
/**
 *가까운 지점부터 방문, 쓰레기 모으다가 돌아가서 쓰레기 비움
 * 1. 양이 용량 도달
 * 지점 쓰레기를 실었을 때 용량 넘을 떄
 * 실을 지점이 없을 때
 *
 * 특정 지점에 실을 때 한 번에 모두 실어야 함 -> 일부 싣기 안 됨
 */
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    int T, W, N;
    // 이거 쓰면 안 됨...
    List<int[]> x;
    long[] answers;

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());
        answers = new long[T];

        for (int i = 0; i < T; i++){
            st = new StringTokenizer(br.readLine());
            W = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());

            x = new ArrayList<>();

            // 거리 입력
            for (int j = 0; j < N; j++){
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                x.add(new int[]{a,b});
            }

            int cur = W;
            int pos = 0;
            int temp = 0;

            for (int[]  ints: x){
                int w =ints[1];
                int key = ints[0];
                if (w> cur) { // 못 담을 때
                    pos += key-temp+ 2*key; // 왔다 갔다
                    cur = W - w;
                } else if (w==cur){ // 딱 담을 때
                    pos += key-temp + 2*key;
                    cur = W;
                } else {
                    pos += key-temp;
                    cur -= w;
                }
//                System.out.println("cur = " + cur);
//                System.out.println("pos = " + pos);
                temp = key;
            }


            if (cur != W){
                pos += temp;
            } else {
                pos -= temp;
            }

            answers[i] = pos;
        }

        for (int i=0; i<T;i++){
            System.out.println(answers[i]);
        }

    }

    public static void main(String args[]) throws Exception{
        new Main().solution();
    }
}
