import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static private class Edge{
		int from, to, weight;

		public Edge(int from, int to, int weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}
		
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(stk.nextToken());
		int E = Integer.parseInt(stk.nextToken());
		
		int start = Integer.parseInt(br.readLine());
//		int[][] adjMatrix = new int[V+1][V+1];
		ArrayList<Edge>[] adj = new ArrayList[V+1];
		for (int i = 1; i < V+1; i++) {
			adj[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < E; i++) {
			stk = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(stk.nextToken());
			int to = Integer.parseInt(stk.nextToken());
			int weight = Integer.parseInt(stk.nextToken());
			
			adj[from].add(new Edge(from, to, weight));
		}
		
		int[] distance = new int[V+1];
		boolean[] visited = new boolean[V+1];
		
		final int INF = Integer.MAX_VALUE;
		Arrays.fill(distance, INF);
		distance[start] = 0;
		
		int min, cur;
		for (int i = 1; i < V+1; i++) {
			cur = -1;
			min = INF;
			
			for (int j = 1; j < V+1; j++) {
				if (!visited[j] && min > distance[j]) {
					cur = j;
					min = distance[j];
				}
			}

			if (cur == -1) break;
			
			visited[cur] = true;
			
			for (Edge edge : adj[cur]) {
				if (!visited[edge.to] && distance[edge.to] > min + edge.weight) {
					distance[edge.to] = min + edge.weight;
				}
			}
			
		}
		
		for (int i = 1; i < V+1; i++) {
			System.out.println(distance[i] == INF ? "INF" : distance[i]);
		}
		
	}

}