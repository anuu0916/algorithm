package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution_3124_D4_최소스패닝트리_안유진 {
	static private class Edge implements Comparable<Edge> {
		int from, to, weight;

		public Edge(int from, int to, int weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return Integer.compare(this.weight, o.weight);
		}

	}

	static int[] parents;
	static Edge[] edgeList;
	static StringTokenizer stk;
	static BufferedReader br;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();

		for (int tc = 1; tc <= T; tc++) {
			stk = new StringTokenizer(br.readLine());
			int V = Integer.parseInt(stk.nextToken());
			int E = Integer.parseInt(stk.nextToken());
			long res = prim(V, E);

			sb.append("#").append(tc).append(" ").append(res).append("\n");
		}

		System.out.print(sb);
	}

	private static void makeSet(int V) {
		parents = new int[V + 1];
		for (int i = 1; i <= V; i++) {
			parents[i] = i;
		}
	}

	private static int findSet(int v) {
		if (parents[v] == v)
			return v;
		return parents[v] = findSet(parents[v]);
	}

	private static boolean union(int u, int v) {
		int root1 = findSet(u);
		int root2 = findSet(v);

		if (root1 == root2)
			return false;

		parents[root2] = root1;
		return true;
	}

	private static long kruskal(int V, int E) throws Exception {

		edgeList = new Edge[E];

		for (int i = 0; i < E; i++) {
			stk = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(stk.nextToken());
			int b = Integer.parseInt(stk.nextToken());
			int c = Integer.parseInt(stk.nextToken());

			edgeList[i] = new Edge(a, b, c);
		}

		makeSet(V);

		Arrays.sort(edgeList);

		int cnt = 0;
		long res = 0;
		for (Edge edge : edgeList) {
			if (union(edge.from, edge.to)) {
				res += edge.weight;
				cnt++;

				if (cnt == V - 1) {
					break;
				}
			}
		}

		return res;
	}

	private static long prim(int V, int E) throws Exception {

		ArrayList<Edge>[] adj = new ArrayList[V + 1];
		for (int i = 0; i <= V; i++) {
			adj[i] = new ArrayList<>();
		}

		for (int i = 0; i < E; i++) {
			stk = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(stk.nextToken());
			int b = Integer.parseInt(stk.nextToken());
			int c = Integer.parseInt(stk.nextToken());

			adj[a].add(new Edge(a, b, c));
			adj[b].add(new Edge(b, a, c));
		}

		boolean[] visited = new boolean[V + 1];
		PriorityQueue<Edge> queue = new PriorityQueue<>();
		queue.addAll(adj[1]);
		visited[1] = true;

		int cnt = 1;
		long res = 0;

		while (cnt != V && !queue.isEmpty()) {
			Edge min = queue.poll();

			if (visited[min.to])
				continue;

			res += min.weight;
			cnt++;
			queue.addAll(adj[min.to]);
			visited[min.to] = true;
		}

		return res;
	}

}