
/**
 * 점화식이 있다
 * t(0) = 1
 * t(n) = sum (t(k) + t(n-1-k)) k 가 0-> n-1
 * t(n)을 출력하긔
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    BigInteger[] t = new BigInteger[36];
    int N;

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        t[0] = new BigInteger("1");

        for (int i = 1; i < N+1; i++){
            BigInteger sum = new BigInteger("0");
            for (int j=0; j<i; j++){

                sum = new BigInteger(
                        sum.add(
                                t[j].multiply(
                                        new BigInteger(t[i-j-1].toString())
                                )
                        ).toString()
                );
            }
            t[i] = sum;
        }

        System.out.println(t[N]);
    }

    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}
