import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] tmp = br.readLine().split(" ");
		StringBuilder sb = new StringBuilder(10);
		
		int n = Integer.parseInt(tmp[0]);
		int m = Integer.parseInt(tmp[1]);
		int[] numbers = new int[n+1];
		
		tmp = br.readLine().split(" ");
		int sum = 0;
		for (int i = 1; i <= n; i++) {
			sum += Integer.parseInt(tmp[i-1]);
			numbers[i] = sum;
		}
		
		int start, end;
		for (int i = 0; i < m; i++) {
			tmp = br.readLine().split(" ");
			start = Integer.parseInt(tmp[0]);
			end = Integer.parseInt(tmp[1]);
			
			sb.append(numbers[end] - numbers[start-1]).append("\n");
		}
		
		System.out.print(sb.toString());
	}
}