import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	private static class Edge implements Comparable<Edge>{
		int to;
		long cost;

		public Edge(int to, long cost) {
			super();
			this.to = to;
			this.cost = cost;
		}

		@Override
		public int compareTo(Edge o) {
			return Long.compare(cost, o.cost);
		}
		
		
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		
		int N = Integer.parseInt(br.readLine());
		ArrayList<Edge>[] adj = new ArrayList[N];
		for (int i = 0; i < N; i++) {
			adj[i] = new ArrayList<>();
		}
		
		boolean[] visited = new boolean[N];
		
		long cost;
		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				cost = Long.parseLong(stk.nextToken());
				if (i == j) continue;
				
				adj[i].add(new Edge(j, cost));
			}
		}
		
		PriorityQueue<Edge> queue = new PriorityQueue<>();
		int cnt = 1;
		long result = 0;
		
		queue.addAll(adj[0]);
		visited[0] = true;
		
		while(cnt != N) {
			Edge min = queue.poll();
			
			if(visited[min.to]) continue;
			
			result += min.cost;
			queue.addAll(adj[min.to]);
			visited[min.to] = true;
			cnt++;
		}
		
		System.out.println(result);
	}

}