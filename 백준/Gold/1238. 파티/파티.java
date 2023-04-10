import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


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

		@Override
		public String toString() {
			return "Edge [v=" + v + ", w=" + w + "]";
		}
		
		
	}
	
	private static final int INF = Integer.MAX_VALUE >> 2;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		
		stk = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(stk.nextToken());
		int M = Integer.parseInt(stk.nextToken());
		int X = Integer.parseInt(stk.nextToken());
		
		List<Edge>[] adj = new ArrayList[N+1];
		List<Edge>[] reverseAdj = new ArrayList[N+1];
		for (int i = 1; i < N+1; i++) {
			adj[i] = new ArrayList<>();
			reverseAdj[i] = new ArrayList<>();
		}
		
		int from, to, cost;
		for (int i = 0; i < M; i++) {
			stk = new StringTokenizer(br.readLine());
			from = Integer.parseInt(stk.nextToken());
			to = Integer.parseInt(stk.nextToken());
			cost = Integer.parseInt(stk.nextToken());
			
			adj[from].add(new Edge(to, cost));
			reverseAdj[to].add(new Edge(from, cost));
		}
		
		// 파티 장소에서 모든 정점으로의 최단거리
		Edge[] fromX = new Edge[N+1];
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		for (int i = 1; i < N+1; i++) {
			if (i == X) {
				fromX[i] = new Edge(i, 0);
			} else {
				fromX[i] = new Edge(i, INF);
			}
			
			pq.add(fromX[i]);
		}
		
		
		boolean[] check = new boolean[N+1];
		while(!pq.isEmpty()) {
			Edge edge = pq.poll();
			
			for (Edge next : adj[edge.v]) {
				if (!check[next.v] && fromX[next.v].w > fromX[edge.v].w + next.w) {
					fromX[next.v].w = fromX[edge.v].w + next.w;
					pq.remove(fromX[next.v]);
					pq.add(fromX[next.v]);
				}
			}
			
			check[edge.v] = true;
		}
		
		
		// 모든 정점에서 파티 장소로 가는 최단거리 (방향을 뒤집은 인접리스트 사용)
		pq.clear();
		Edge[] toX = new Edge[N+1];
		for (int i = 1; i < N+1; i++) {
			if (i == X) {
				toX[i] = new Edge(i, 0);
			} else {
				toX[i] = new Edge(i, INF);
			}
			
			pq.add(toX[i]);
		}
		
		Arrays.fill(check, false);
		while(!pq.isEmpty()) {
			Edge edge = pq.poll();
			
			for (Edge next : reverseAdj[edge.v]) {
				if (!check[next.v] && toX[next.v].w > toX[edge.v].w + next.w) {
					toX[next.v].w = toX[edge.v].w + next.w;
					pq.remove(toX[next.v]);
					pq.add(toX[next.v]);
				}
			}
			
			check[edge.v] = true;
		}
		
		
		int max = 0;
		for (int i = 1; i < N+1; i++) {
			max = Math.max(max, toX[i].w + fromX[i].w);
		}
		
		System.out.println(max);
		
	}

}