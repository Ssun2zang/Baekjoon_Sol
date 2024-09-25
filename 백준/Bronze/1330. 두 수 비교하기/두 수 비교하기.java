import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    int A, B;
    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        
        if (A <B){
            System.out.println("<");
        } else if (A > B){
            System.out.println(">");
        } else {
            System.out.println("==");
        }
    }
    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}