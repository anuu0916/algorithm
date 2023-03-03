package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_2001_D2_파리퇴치_안유진 {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder(10);
		String[] tmp;
		int N, M;
		int[][] dp;
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= T; test_case++) {
			tmp = br.readLine().split(" ");
			N = Integer.parseInt(tmp[0]);
			M = Integer.parseInt(tmp[1]);
			dp = new int[N+1][N+1];
			
			// 배열 입력
			for (int i = 1; i <= N; i++) {
				tmp = br.readLine().split(" ");
				for (int j = 1; j <= N; j++) {
					// 누적합 계산
					dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + Integer.parseInt(tmp[j-1]);
				}
			}
			
			int max = 0; // 최댓값 (죽은 파리의 개수)
			int sum = 0; // MxM 배열 파리의 합
			for (int i = M; i <= N; i++) {
				for (int j = M; j <= N; j++) {
					sum = dp[i][j] - dp[i-M][j] - dp[i][j-M] + dp[i-M][j-M];
					max = Math.max(max, sum);
				}
			}
			
			sb.append("#").append(test_case).append(" ").append(max).append("\n");
		}
		
		System.out.print(sb.toString());

	}

}
