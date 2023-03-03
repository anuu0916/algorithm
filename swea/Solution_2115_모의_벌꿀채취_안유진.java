package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_2115_모의_벌꿀채취_안유진 {
	private static class Honey{
		int row, start;

		public Honey() {}

		@Override
		public String toString() {
			StringBuilder builder = new StringBuilder();
			builder.append("Honey [row=").append(row).append(", start=").append(start).append("]");
			return builder.toString();
		}

		
		
	}
	
	static int N, M, C, max;
	static int max1, max2;
	static int[][] map;
	static int[] box1, box2;
	static boolean[] isSelected;
	static Honey h1 = new Honey(), h2 = new Honey();

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine().trim());
		
		for (int tc = 1; tc <= T; tc++) {
			stk = new StringTokenizer(br.readLine());
			N = Integer.parseInt(stk.nextToken());
			M = Integer.parseInt(stk.nextToken());
			C = Integer.parseInt(stk.nextToken());
			
			map = new int[N][N];
			box1 = new int[M];
			box2 = new int[M];
			max = 0;
			
			for (int i = 0; i < N; i++) {
				stk = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(stk.nextToken());
				}
			}
			
			select1();
			
			sb.append("#").append(tc).append(" ").append(max).append("\n");
		}
		
		System.out.print(sb);
	}

	private static void select1() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N-M+1; j++) {
				h1.row = i;
				h1.start = j;
				select2();
			}
		}
	}

	private static void select2() {
		for (int i = h1.row; i < N; i++) {
			for (int j = 0; j < N-M+1; j++) {
				if (i == h1.row && j < h1.start + M) continue;
				h2.row = i;
				h2.start = j;
				
				getProfit();
			}
		}
	}

	private static void getProfit() {
		for (int i = 0; i < M; i++) {
			box1[i] = map[h1.row][h1.start+i];
			box2[i] = map[h2.row][h2.start+i];
		}
		
		isSelected = new boolean[M];
		max1 = 0;
		subset1(0);
		
		isSelected = new boolean[M];
		max2 = 0;
		subset2(0);
		
		max = Math.max(max1+max2, max);
		
	}

	private static void subset1(int cnt) {
		if (cnt == M) {
			int sum = 0;
			int profit = 0;
			for (int i = 0; i < M; i++) {
				if (isSelected[i]) {
					sum += box1[i];
					profit += box1[i] * box1[i];
				}
			}
			
			if (sum > C) return;
			
			max1 = Math.max(max1, profit);
			return;
		}
		
		isSelected[cnt] = true;
		subset1(cnt+1);
		isSelected[cnt] = false;
		subset1(cnt+1);
	}
	
	private static void subset2(int cnt) {
		if (cnt == M) {
			int sum = 0;
			int profit = 0;
			for (int i = 0; i < M; i++) {
				if (isSelected[i]) {
					sum += box2[i];
					profit += box2[i] * box2[i];
				}
			}
			
			if (sum > C) return;
			
			max2 = Math.max(max2, profit);
			return;
		}
		
		isSelected[cnt] = true;
		subset2(cnt+1);
		isSelected[cnt] = false;
		subset2(cnt+1);
	}

	

}
