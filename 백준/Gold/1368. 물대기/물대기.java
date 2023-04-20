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
		
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		for (int i = 0; i < N; i++) {
			pq.add(new Edge(i, Integer.parseInt(br.readLine())));
		}
		
		ArrayList<Edge>[] adj = new ArrayList[N];
		
		for (int i = 0; i < N; i++) {
			adj[i] = new ArrayList<>();
		}
		
		int cost = 0;
		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				cost = Integer.parseInt(stk.nextToken());
				if (i==j) continue;
				adj[i].add(new Edge(j, cost));
			}
		}
		
		
		boolean[] visited = new boolean[N];
		int result = 0;
		int cnt = 0;
		
		while(cnt < N) {
			Edge min = pq.poll();
			
			if (visited[min.to]) continue;
			
			result += min.cost;
			pq.addAll(adj[min.to]);
			visited[min.to] = true;
			cnt++;
		}
		
		System.out.println(result);
		
	}

}