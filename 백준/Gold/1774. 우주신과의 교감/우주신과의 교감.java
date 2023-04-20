import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	private static class Pos {
		int x, y;

		public Pos(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
		
	}
	
	private static class Edge implements Comparable<Edge> {
		int from, to;
		double cost;

		public Edge(int from, int to, double cost) {
			super();
			this.from = from;
			this.to = to;
			this.cost = cost;
		}

		@Override
		public int compareTo(Edge o) {
			return Double.compare(cost, o.cost);
		}

	}
	
	static int[] parents;
	static Pos[] godList;
	static int N, M;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		
		parents = new int[N];
		
		for (int i = 0; i < N; i++) {
			makeSet(i);
		}
		
		godList = new Pos[N];
		
		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			godList[i] = new Pos(Integer.parseInt(stk.nextToken()), Integer.parseInt(stk.nextToken()));
		}
		
		List<Edge> adjList = new ArrayList<Edge>();
		for (int i = 0; i < N; i++) {
			for (int j = i; j < N; j++) {
				if (i==j) continue;
				adjList.add(new Edge(i, j, getDist(i, j)));
			}
		}
		
		for (int i = 0; i < M; i++) {
			stk = new StringTokenizer(br.readLine());
			union(Integer.parseInt(stk.nextToken()) - 1, Integer.parseInt(stk.nextToken()) - 1);
		}
		
		double result = 0;
		Collections.sort(adjList);
		
		for (Edge edge : adjList) {
			if (union(edge.to, edge.from)) {
				result += edge.cost;
				if (checkConnection()) break;
			}
		}
		
		System.out.printf("%.2f\n", result);
		
	}

	private static boolean checkConnection() {
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			if (parents[i] == i) cnt++;
		}
		
		if (cnt > 1) return false;
		else return true;
	}

	private static double getDist(int i, int j) {
		return Math.sqrt(Math.pow(godList[i].x - godList[j].x, 2) + Math.pow(godList[i].y - godList[j].y, 2));
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
		return parents[v] = findSet(parents[v]);
	}

	private static void makeSet(int v) {
		parents[v] = v;
	}

}