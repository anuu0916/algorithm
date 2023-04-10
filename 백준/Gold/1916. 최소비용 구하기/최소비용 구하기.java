import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.io.BufferedReader;

public class Main {
	private static class Edge implements Comparable<Edge> {
		int v, w;

		public Edge(int v, int w) {
			super();
			this.v = v;
			this.w = w;
		}

		@Override
		public int compareTo(Edge o) {
			return Integer.compare(w, o.w);
		}
		
		
	}
	
	private static final int INF = Integer.MAX_VALUE >> 2;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		List<Edge>[] adj = new ArrayList[N+1];
		for (int i = 1; i < N+1; i++) {
			adj[i] = new ArrayList<>();
		}
		
		int from, to, cost; 
		for (int i = 0; i < M; i++) {
			stk = new StringTokenizer(br.readLine());
			from = Integer.parseInt(stk.nextToken());
			to = Integer.parseInt(stk.nextToken());
			cost = Integer.parseInt(stk.nextToken());
			
			adj[from].add(new Edge(to, cost));
		}
		
		// 출발점의 도시번호와 도착점의 도시번호
		stk = new StringTokenizer(br.readLine());
		from = Integer.parseInt(stk.nextToken());
		to = Integer.parseInt(stk.nextToken());
		
		Edge[] D = new Edge[N+1];
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		
		// 출발점 : from
		for (int i = 1; i < N+1; i++) {
			if (i == from) {
				D[i] = new Edge(i, 0);
			} else {
				D[i] = new Edge(i, INF);
			}
			
			pq.add(D[i]);
		}
		
		
		boolean[] check = new boolean[N+1];
		
		while(!pq.isEmpty()) {
			Edge edge = pq.poll();
			
			for (Edge next : adj[edge.v]) {
				if (!check[next.v] && D[next.v].w > D[edge.v].w + next.w) {
					D[next.v].w = D[edge.v].w + next.w;
					pq.remove(D[next.v]);
					pq.add(D[next.v]);
				}
			}
			
			check[edge.v] = true;
		}
		
		System.out.println(D[to].w);
		
	}

}