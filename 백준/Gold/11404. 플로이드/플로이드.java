import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	private static final int INF = Integer.MAX_VALUE >> 2;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		int[][] map = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			Arrays.fill(map[i], INF);
		}
		
		int to, from, cost;
		for (int i = 0; i < M; i++) {
			stk = new StringTokenizer(br.readLine());
			from = Integer.parseInt(stk.nextToken()) - 1;
			to = Integer.parseInt(stk.nextToken()) - 1;
			cost = Integer.parseInt(stk.nextToken());
			
			map[from][to] = Math.min(map[from][to], cost);
			
		}
		
		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				if (i==k) continue;
				for (int j = 0; j < N; j++) {
					if (i == j || j==k) continue;
					
					if (map[i][j] > map[i][k] + map[k][j]) {
						map[i][j] = map[i][k] + map[k][j];
					}
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (map[i][j] == INF) sb.append(0).append(" ");
				else sb.append(map[i][j]).append(" ");
			}
			sb.append("\n");
		}
		
		System.out.print(sb);
		
	}

}