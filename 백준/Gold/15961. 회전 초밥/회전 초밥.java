import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, d, k, c;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(stk.nextToken());
		d = Integer.parseInt(stk.nextToken());
		k = Integer.parseInt(stk.nextToken());
		c = Integer.parseInt(stk.nextToken());
		
		int[] sushi = new int[N];
		for (int i = 0; i < N; i++) {
			sushi[i] = Integer.parseInt(br.readLine());
		}
		
		int types = 1;
		int[] eaten = new int[d+1];
		eaten[c] = 1;
		
		// 처음 k개
		for (int i = 0; i < k; i++) {
			if (eaten[sushi[i]] == 0) {
				types++;
			}
			eaten[sushi[i]]++;
		}
		
		int max = types;
		for (int i = k; i < N+k; i++) {
			if (--eaten[sushi[(i-k) % N]] == 0) {
				types--;
			}
			
			if (eaten[sushi[i%N]]++ == 0) {
				types++;
			}
			
			max = Math.max(max, types);
		}
		
		
		System.out.println(max);
	}


}