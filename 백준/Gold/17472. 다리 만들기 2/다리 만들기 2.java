import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static class Edge implements Comparable<Edge>{
		int from, to, w;

		public Edge(int from, int to, int w) {
			super();
			this.from = from;
			this.to = to;
			this.w = w;
		}
        
		@Override
		public int compareTo(Edge o) {
			return Integer.compare(w, o.w);
		}
	}
	
	static int N, M, V;
	static int[][] map;
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	static int[] parents;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		map = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(stk.nextToken());
			}
		}
		
		label();
		
		// 놓을 수 있는 다리 구하기
		Queue<Edge> pq = new PriorityQueue<Edge>();
		
		int nr, nc, cnt;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] != 0) {
					for (int k = 0; k < 4; k++) {
						nr = i + dr[k];
						nc = j + dc[k];
						cnt = 0;
						
						while(isValid(nr, nc)) {
							if (map[nr][nc] == map[i][j]) break;
							if (map[nr][nc] > 0 && cnt < 2) break;
							
							if (map[nr][nc] > 0) {
								Edge edge = new Edge(map[i][j], map[nr][nc], cnt);
								pq.add(edge);
								break;
							}
							
							nr += dr[k];
							nc += dc[k];
							cnt++;
						}
					}
				}
			}
		}
		
		
		parents = new int[V];
		makeSet();
		
		int result = 0;
		Edge edge;
		while(!pq.isEmpty()) {
			edge = pq.poll();
			if (union(edge.from, edge.to)) {
				result += edge.w;
				if(isConnected()) break;
			}
		}
		
		if (!isConnected()) System.out.println(-1);
		else System.out.println(result);
		
	}

	private static boolean isConnected() {
		int cnt = 0;
		for (int i = 1; i < V; i++) {
			if (parents[i] == i) cnt++;
		}
		
		if (cnt == 1) return true;
		return false;
	}

	private static void label() {
		Queue<int[]> queue = new ArrayDeque<int[]>();
		boolean[][] visited = new boolean[N][M];
		int num = 1;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 1 && !visited[i][j]) {
					queue.add(new int[] {i, j});
					visited[i][j] = true;
					
					while(!queue.isEmpty()) {
						int[] cur = queue.poll();
						map[cur[0]][cur[1]] = num;
						
						for (int k = 0; k < 4; k++) {
							int nr = cur[0] + dr[k];
							int nc = cur[1] + dc[k];
							
							if (!isValid(nr, nc) || visited[nr][nc] || map[nr][nc] != 1) continue;
							
							queue.add(new int[] {nr, nc});
							visited[nr][nc] = true;
						}
						
					}
					
					num++;
				}
			}
		}
		
		V = num;
	}

	private static void makeSet() {
		for (int i = 0, size = parents.length; i < size ; i++) {
			parents[i] = i;
		}
	}
	
	private static boolean union(int v, int u) {
		int root1 = findSet(v);
		int root2 = findSet(u);
		
		if (root1 == root2) return false;
		
		parents[root1] = root2;
		return true;
	}

	private static int findSet(int v) {
		if (parents[v] == v) return v;
		else return parents[v] = findSet(parents[v]);
	}

	private static boolean isValid(int nr, int nc) {
		if (nr < 0 || nr >= N || nc < 0 || nc >= M) return false;
		return true;
	}

}