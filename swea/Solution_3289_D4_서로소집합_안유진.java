package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_3289_D4_서로소집합_안유진 {
	static int[] parents;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			stk = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(stk.nextToken());
			int M = Integer.parseInt(stk.nextToken());
			
			parents = new int[N+1];
			sb.append("#").append(tc).append(" ");
			
			for (int i = 1; i <= N; i++) {
				makeSet(i);
			}
			
			for (int i = 0; i < M; i++) {
				stk = new StringTokenizer(br.readLine());
				if (stk.nextToken().equals("0")) {
					int u = Integer.parseInt(stk.nextToken());
					int v = Integer.parseInt(stk.nextToken());
					union(u, v);
				} else {
					int u = Integer.parseInt(stk.nextToken());
					int v = Integer.parseInt(stk.nextToken());
					
					if (findSet(u) == findSet(v)) {
						sb.append(1);
					} else {
						sb.append(0);
					}
				}
			}
			
			sb.append("\n");
		}
		
		System.out.print(sb);
	}

	public static void makeSet(int v) {
		parents[v] = v;
	}
	
	public static int findSet(int v) {
		if (parents[v] == v) return v;
		return parents[v] = findSet(parents[v]);
	}
	
	public static void union(int u, int v) {
		parents[findSet(u)] = findSet(v);
	}

}
