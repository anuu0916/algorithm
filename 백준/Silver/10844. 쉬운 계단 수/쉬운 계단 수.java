import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long mod = 1000000000;
		long[][] dp = new long[N+1][10];
		
		// 첫 번째 자릿수 (왼쪽에서 첫 번째)는 경우의 수가 하나뿐임 (숫자를 지정해줌)
		for (int i = 1; i < 10; i++) {
			dp[1][i] = 1;
		}
		
		// 두 번째 자릿수부터 N번째 자리수까지 탐색
		for (int i = 2; i < N+1; i++) {
			// 현재 자리값을 0부터 9까지 탐색
			for (int j = 0; j < 10; j++) {
				// 현재 자릿수 9라면 이전 자릿수는 8만 가능
				if (j == 9) {
					dp[i][9] = dp[i-1][8] % mod;
				}
				// 현재 자릿수가 0이라면 이전 자릿수는 1만 가능
				else if (j==0) {
					dp[i][0] = dp[i-1][1] % mod;
				}
				// 그 외는 1씩 차이나는 숫자 가능
				else {
					dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod;
				}
			}
		}
		
		long ans = 0;
		for (int i = 0; i < 10; i++) {
			ans += dp[N][i];
		}
		
		System.out.println(ans%mod);
	}

}