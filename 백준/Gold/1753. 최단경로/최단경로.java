import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static private class Edge implements Comparable<Edge>{
		int to, weight;

		public Edge(int to, int weight) {
			super();
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return Integer.compare(this.weight, o.weight);
		}
		
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(stk.nextToken());
		int E = Integer.parseInt(stk.nextToken());
		
		int start = Integer.parseInt(br.readLine());
		ArrayList<Edge>[] adj = new ArrayList[V+1];
		for (int i = 1; i < V+1; i++) {
			adj[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < E; i++) {
			stk = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(stk.nextToken());
			int to = Integer.parseInt(stk.nextToken());
			int weight = Integer.parseInt(stk.nextToken());
			
			adj[from].add(new Edge(to, weight));
		}
		
		int[] distance = new int[V+1];
		PriorityQueue<Edge> queue = new PriorityQueue<>();
		final int INF = Integer.MAX_VALUE;
		Arrays.fill(distance, INF);
		queue.offer(new Edge(start, 0));
		distance[start] = 0;
		
		while(!queue.isEmpty()) {
			Edge cur = queue.poll();
			int v = cur.to;
			int w = cur.weight;
			if (distance[v] < w) continue;
			
			for (Edge edge : adj[v]) {
				if(distance[edge.to] > w + edge.weight) {
					distance[edge.to] = w + edge.weight;
					queue.offer(new Edge(edge.to, distance[edge.to]));
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i < V+1; i++) {
			sb.append(distance[i] == INF ? "INF" : distance[i]).append("\n");
		}
		
		System.out.print(sb);
	}

}