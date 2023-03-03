package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Solution_7465_D4_창용마을무리의개수_안유진 {
	static int[] parents;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			stk = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(stk.nextToken());
			int M = Integer.parseInt(stk.nextToken());
			
			parents = new int[N+1];
			for (int i = 1; i <= N; i++) {
				makeSet(i);
			}
			
			int u, v;
			for (int i = 0; i < M; i++) {
				stk = new StringTokenizer(br.readLine());
				u = Integer.parseInt(stk.nextToken());
				v = Integer.parseInt(stk.nextToken());
				
				union(u, v);
			}
			
			Set<Integer> set = new HashSet<Integer>();
			for (int i = 1; i <= N; i++) {
				set.add(findSet(i));
			}
			
			sb.append("#").append(tc).append(" ").append(set.size()).append("\n");
		}
		
		System.out.print(sb);
	}
	
	private static void makeSet(int v) {
		parents[v] = v;
	}
	
	private static int findSet(int v) {
		if (parents[v] == v) return v;
		return parents[v] = findSet(parents[v]);
	}
	
	private static void union(int u, int v) {
		parents[findSet(u)] = findSet(v);
	}

}
