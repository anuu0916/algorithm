package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_1767_프로세서연결하기_안유진 {
	private static class Pos {
		int r, c;

		public Pos(int r, int c) {
			super();
			this.r = r;
			this.c = c;
		}

		@Override
		public String toString() {
			StringBuilder builder = new StringBuilder();
			builder.append("Pos [r=").append(r).append(", c=").append(c).append("]");
			return builder.toString();
		}

	}

	static int N, C, M;
	static int res;
	static int max;
	static int[][] origin;
	static boolean[] isSelected;
	static ArrayList<Pos> core;
	static ArrayList<Pos> coreList;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringTokenizer stk;
		StringBuilder sb = new StringBuilder(10);
//		int[][] map;

		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine().trim());

			// 초기화
			origin = new int[N][N];
			C = 0; 
			M = 0;
			res = Integer.MAX_VALUE;
			max = 0;
			int border = 0;
			coreList = new ArrayList<>(12);
			
			// map 입력
			for (int i = 0; i < N; i++) {
				stk = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					origin[i][j] = Integer.parseInt(stk.nextToken());
					if (i == 0 || i == N - 1 || j == 0 || j == N - 1) {
						border++;
						continue;
					}
					if (origin[i][j] == 1) {
						coreList.add(new Pos(i, j));
						C++;
					}
				}
			}
			
			isSelected = new boolean[C];

			subset(0);
			
			if (res == Integer.MAX_VALUE && border> 0) {
				res = 0;
			}
			
			sb.append("#").append(tc).append(" ").append(res).append("\n");
		}

		System.out.print(sb);
	}

	private static void subset(int cnt) {
		if (cnt == C) {
			core = new ArrayList<>();
			for (int i = 0; i < C; i++) {
				if (isSelected[i])
					core.add(coreList.get(i));
			}

			if (core.isEmpty())
				return;

			M = core.size();
			if (max > M)
				return;
			
			int[][] copied = new int[N][N];
			copy(origin, copied);
			connect(copied, 0, 0);

			return;
		}

		isSelected[cnt] = true;
		subset(cnt + 1);

		isSelected[cnt] = false;
		subset(cnt + 1);
	}
	
	private static void printArr(int[][] map) {
		
		System.out.println("================");
		System.out.println(core.toString());
		for (int[] is : map) {
			System.out.println(Arrays.toString(is));
		}
	}

	private static void connect(int[][] map, int cnt, int sum) {
		if (cnt == M) {
//			printArr(map);
			
			if (M > max) {
				max = M;
				res = sum;
			}
			else if (M == max) res = Math.min(res, sum);
			
			return;
		}

		Pos c = core.get(cnt);

		int nr = c.r, nc = c.c;
		boolean flag = true;
		int len = 0;

		for (int dir = 0; dir < 4; dir++) {
			flag = true;
			nr = c.r;
			nc = c.c;
			while (true) {
				nr += dr[dir];
				nc += dc[dir];

				if (nr < 0 || nr >= N || nc < 0 || nc >= N) {
					break;
				}
				if (map[nr][nc] == 1) {
					flag = false;
					break;
				}

			}

			if (!flag) {
				continue;
			}

			int[][] copied = new int[N][N];
			copy(map, copied);
			
			len = 0;
			nr = c.r;
			nc = c.c;
			while (true) {
				nr += dr[dir];
				nc += dc[dir];

				if (nr < 0 || nr >= N || nc < 0 || nc >= N) {
					break;
				}

				copied[nr][nc] = 1;
				len++;

			}

			connect(copied, cnt + 1, sum + len);

		}

	}

	private static void copy(int[][] map, int[][] copied) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				copied[i][j] = map[i][j];
			}
		}
	}

}
