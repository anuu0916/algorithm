import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] st1 = br.readLine().toCharArray();
		char[] st2 = br.readLine().toCharArray();
		
		int len1 = st1.length;
		int len2 = st2.length;
		int[][] dp = new int[len1+1][len2+1];
		
		for (int i = 1; i <= len1; i++) {
			for (int j = 1; j <= len2; j++) {
				if (st1[i-1] == st2[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
				else dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
			}
		}
		
		System.out.println(dp[len1][len2]);
	}

}