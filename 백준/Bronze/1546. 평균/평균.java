import java.io.*;
import java.util.*; 

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

	    int N = Integer.parseInt(st.nextToken());

	    int[] nums = new int[N];
	    int maxVal = -1;
	
	    st = new StringTokenizer(br.readLine());
	    for (int i = 0; i < N; i++){
            nums[i] = Integer.parseInt(st.nextToken());
		    maxVal = Math.max(nums[i], maxVal);
	    }	

	    float sum = 0;
	
	    for (int i = 0; i < N; i++){
		      sum += ((float)nums[i]/maxVal)*100;
	    }

	    System.out.println(sum/N);
    }
}