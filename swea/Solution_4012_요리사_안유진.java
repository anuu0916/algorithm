package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_4012_요리사_안유진 {
	private static int ans = Integer.MAX_VALUE;
	private static int[][] S;
	private static boolean[] isSelected;
	private static int N;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());
			S = new int[N][N];
			isSelected = new boolean[N];
			ans = Integer.MAX_VALUE;
			
			for (int i = 0; i < N; i++) {
				stk = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					S[i][j] = Integer.parseInt(stk.nextToken());
				}
				
			}
			
			combi(0, 0);
			
			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		}
		
		System.out.print(sb);

	}

	private static void combi(int cnt, int start) {
		if (cnt == N/2) {
			int sum1 = 0, sum2 = 0;
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (isSelected[i] && isSelected[j])
						sum1 += S[i][j];
					else if (!isSelected[i] && !isSelected[j])
						sum2 += S[i][j];
				}
			}
			
			ans = Math.min(ans, Math.abs(sum1-sum2));
			return;
		}
		
		for (int i = start; i < N; i++) {
			isSelected[i] = true;
			combi(cnt+1, i+1);
			isSelected[i] = false;
		}
		
	}
	
	

}
