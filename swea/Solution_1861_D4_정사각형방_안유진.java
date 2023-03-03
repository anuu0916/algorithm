package swea;

import java.util.Scanner;

public class Solution_1861_D4_정사각형방_안유진 {
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int[][] map;
	static int N, res_num, max;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int test_case = 1; test_case <= T; test_case++) {
			N = sc.nextInt();
			map = new int[N + 2][N + 2];
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					map[i][j] = sc.nextInt();
				}
			}

			max = 0;
			res_num = N*N;
			for (int x = 1; x <= N; x++) {
				for (int y = 1; y <= N; y++) {
					dfs(x, y, x, y, 1);
				}
			}

			System.out.printf("#%d %d %d\n", test_case, res_num, max);

		}

	}

	private static void dfs(int x, int y, int cr, int cc, int dis) {
		if (max < dis) {
			max = dis;
			res_num = map[x][y];
		} else if (max == dis) {
			max = dis;
			res_num = Math.min(res_num, map[x][y]);
		}
		
		for (int i = 0; i < 4; i++) {
			int nr = cr + dr[i];
			int nc = cc + dc[i];

			if (map[nr][nc] == (map[cr][cc] + 1)) {
				dfs(x, y, nr, nc, dis+1);
			}
		}
	}

}
