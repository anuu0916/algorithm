import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int[] parents, truth;
	static int truthNum;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(stk.nextToken());
		int M = Integer.parseInt(stk.nextToken());
		
		parents = new int[N+1];
		for (int i = 1; i <= N; i++) {
			makeSet(i);
		}
		
		// 진실을 아는 사람
		stk = new StringTokenizer(br.readLine());
		truthNum = Integer.parseInt(stk.nextToken());
		
		if (truthNum == 0) {
			System.out.println(M);
			System.exit(0);
		}
		
		truth = new int[truthNum];
		
		for (int i = 0; i < truthNum; i++) {
			truth[i] = Integer.parseInt(stk.nextToken());
			if (i > 0) union(truth[i-1], truth[i]);
		}
		
		// 파티
		int size;
		ArrayList<Integer>[] party = new ArrayList[M];
		for (int p = 0; p < M; p++) {
			stk = new StringTokenizer(br.readLine());
			size = Integer.parseInt(stk.nextToken());
			party[p] = new ArrayList<>();
			
			for (int i = 0; i < size; i++) {
				party[p].add(Integer.parseInt(stk.nextToken()));
				
				if (i > 0) union(party[p].get(i-1), party[p].get(i));
			}
		}
		
		int answer = 0;
		for (ArrayList<Integer> p : party) {
			if (canLie(p)) answer++;
		}
		
		System.out.println(answer);
	}

	private static boolean canLie(ArrayList<Integer> p) {
		for (int n : p) {
			if(findSet(truth[0]) == findSet(n)) return false;
		}
		return true;
	}

	private static void union(int u, int v) {
		parents[findSet(u)] = findSet(v);
	}

	private static int findSet(int v) {
		if (parents[v] == v) return v;
		return parents[v] = findSet(parents[v]);
	}

	private static void makeSet(int v) {
		parents[v] = v;
	}


}