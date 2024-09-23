import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    int max;
    int index = 1;

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        max = Integer.parseInt(st.nextToken());

        int val;
        for (int i = 0; i < 8; i++) {
            st = new StringTokenizer(br.readLine());
            val = Integer.parseInt(st.nextToken());
            if (max < val) {
                max = val;
                index = i + 2;
            }

        }

        System.out.println(max);
        System.out.println(index);
    }
    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}