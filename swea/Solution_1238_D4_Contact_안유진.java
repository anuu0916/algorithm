package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution_1238_D4_Contact_안유진 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		StringBuilder sb = new StringBuilder(10);
		boolean[][] adj;
		
		for (int tc = 1; tc <= 10; tc++) {
			stk = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(stk.nextToken());
			int start = Integer.parseInt(stk.nextToken());
			
			adj = new boolean[101][101];
			stk = new StringTokenizer(br.readLine(), " ");
			for (int i = 0; i < N; i+=2) {
				int from = Integer.parseInt(stk.nextToken());
				int to = Integer.parseInt(stk.nextToken());
				
				adj[from][to] = true;
			}
			
			Queue<Integer> queue = new ArrayDeque<Integer>();
			boolean[] visited = new boolean[101];
			queue.offer(start);
			visited[start] = true;
			
			int res = start;
			while(!queue.isEmpty()) {
				int max = 0;
				for (int i = 0, size = queue.size(); i < size; i++) {
					int cur = queue.poll();
					max = Math.max(cur, max);
					
					for (int j = 1; j < 101; j++) {
						if (adj[cur][j] && !visited[j]) {
							queue.offer(j);
							visited[j] = true;
						}
					}
				}
				res = max;
			}
			
			sb.append("#").append(tc).append(" ").append(res).append("\n");
		}
		System.out.print(sb);
	}

}
