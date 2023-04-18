import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	private static class Edge implements Comparable<Edge> {
		int to, cost;

		public Edge(int to, int cost) {
			super();
			this.to = to;
			this.cost = cost;
		}

		@Override
		public int compareTo(Edge o) {
			return Integer.compare(cost, o.cost);
		}
		
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		ArrayList<Edge>[] adj = new ArrayList[N+1];
		for (int i = 1; i < N+1; i++) {
			adj[i] = new ArrayList<>();
		}
		
		int from , to, cost;
		for (int i = 0; i < M; i++) {
			stk = new StringTokenizer(br.readLine());
			from = Integer.parseInt(stk.nextToken());
			to = Integer.parseInt(stk.nextToken());
			cost = Integer.parseInt(stk.nextToken());
			
			adj[from].add(new Edge(to, cost));
			adj[to].add(new Edge(from, cost));
		}
		
		PriorityQueue<Edge> queue = new PriorityQueue<>();
		queue.addAll(adj[1]);
		boolean[] visited = new boolean[N+1];
		visited[1] = true;
		
		int cnt = 1;
		int result = 0;
		
		Edge min;
		while(cnt != N) {
			min = queue.poll();
			
			if (visited[min.to]) continue;
			
			result += min.cost;
			visited[min.to] = true;
			queue.addAll(adj[min.to]);
			cnt++;
		}
		
		System.out.println(result);
	}

}