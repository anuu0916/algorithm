import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	private static final int INF = Integer.MAX_VALUE >> 2;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		
		stk = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(stk.nextToken());
		int E = Integer.parseInt(stk.nextToken());
		
		int[][] map = new int[V][V];
		for (int i = 0; i < V; i++) {
			Arrays.fill(map[i], INF);
		}
		
		int from, to, cost;
		for (int i = 0; i < E; i++) {
			stk = new StringTokenizer(br.readLine());
			
			from = Integer.parseInt(stk.nextToken()) - 1;
			to = Integer.parseInt(stk.nextToken()) - 1;
			cost = Integer.parseInt(stk.nextToken());
			
			map[from][to] = cost;
		}
		
		for (int k = 0; k < V; k++) {
			for (int i = 0; i < V; i++) {
				if (i == k) continue;
				for (int j = 0; j < V; j++) {
					if (j == k || i == j) continue;
					
					if(map[i][j] > map[i][k] + map[k][j]) {
						map[i][j] = map[i][k] + map[k][j];
					}
				}
			}
		}
		
		
		int ans = INF;
		
		for (int i = 0; i < V; i++) {
			for (int j = i+1; j < V; j++) {
				ans = Math.min(ans, map[i][j] + map[j][i]);
			}
		}
		
		if (ans == INF) System.out.println(-1);
		else System.out.println(ans);
	}

}