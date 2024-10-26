
import java.io.*;
import java.util.*;

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[] nums = new int[N];

        String[] nmv = br.readLine().split(" ");
        for (int i = 0; i <N; i++){
            nums[i] = Integer.parseInt(nmv[i]);
        }

        int max = nums[0];
        int min = nums[0];

        for (int n: nums){
            if (n > max){
                max = n;
            }
            if (n < min){
                min = n;
            }
        }

        System.out.print(min);
        System.out.print(" ");
        System.out.println(max);



    }
}