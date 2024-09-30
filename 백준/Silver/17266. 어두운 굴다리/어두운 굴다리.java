import java.io.*;
import java.util.*;

/**
 * 굴다리의 길 0-N을 밝히려고 함
 * M개와 위치 x를 결정함
 * 가로등의 높이만큼 주위를 비출 수 있음
 * 모두 높이가 같아야하고, 정수이다
 * 왼쪽 오른쪽 다 H만큼 밝힘
 */

public class Main {
    int n, m;
    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());


        int past = 0;
        int temp = Integer.parseInt(st.nextToken());
        int answer = temp;

        for (int i = 1; i < m; i++){
            temp = Integer.parseInt(st.nextToken());
            if (temp - past - answer > answer){
                answer = (temp-past)%2 == 1? (temp-past)/2+1 : (temp-past)/2;
            }
            past = temp;
        }
        if (n-past > answer){
            answer = n - past;
        }

        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}
