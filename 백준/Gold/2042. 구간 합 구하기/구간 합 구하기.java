import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, M, K;
	static long[] tree;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		K = Integer.parseInt(stk.nextToken());
		
		long[] nums = new long[N];
		
		for (int i = 0; i < N; i++) {
			nums[i] = Long.parseLong(br.readLine());
		}
		
		tree = new long[N+1];
		
		for (int i = 1; i <= N; i++) {
			update(i, nums[i-1]);
		}
		
		int a, b;
		for (int i = 0; i < M+K; i++) {
			stk = new StringTokenizer(br.readLine());
			a = Integer.parseInt(stk.nextToken());
			b = Integer.parseInt(stk.nextToken());
			
			if (a == 1) {
				long c = Long.parseLong(stk.nextToken());
				update(b, c -nums[b-1]);
				nums[b-1] = c;
			} else {
				int c = Integer.parseInt(stk.nextToken());
				sb.append(sum(b, c)).append("\n");
			}
		}
		
		System.out.print(sb);
		
	}
	
	/**
	 * 입력값으로 tree를 구성하는 함수
	 * 
	 * @param i
	 * @param num
	 */
	private static void update(int i, long num) {
		while(i <= N) {
			tree[i] += num;
			i += (i & -i); // 다음 위치(index + k)에 데이터를 update
			// 음수를 & 해주면 k값을 구할 수 있다.
		}
	}
	
	/**
	 * 1~i까지의 구간합 구하기
	 */
	private static long sum(int i) {
		long ans = 0;
		
		while(i > 0) {
			ans += tree[i];
			i -= (i & -i); // 이전 구간합 구하기
		}
		
		return ans;
	}
	
	/**
	 * start~end까지의 구간합 구하기
	 */
	private static long sum(int start, int end) {
		return sum(end) - sum(start-1);
	}
	
}