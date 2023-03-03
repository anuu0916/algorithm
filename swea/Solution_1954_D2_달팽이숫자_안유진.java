package swea;

import java.util.Scanner;

public class Solution_1954_D2_달팽이숫자_안유진 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		int[] dr = { 0, 1, 0, -1 };
		int[] dc = { 1, 0, -1, 0 };

		for (int test_case = 1; test_case <= T; test_case++) {
			int n = sc.nextInt();
			int[][] arr = new int[n][n];
			int cnt = 1; // 진행 개수
			int dir = 0; // 방향 index
			int r = 0, c = 0;

			arr[r][c] = cnt++;

			while (cnt <= n * n) {
				int nr = r + dr[dir];
				int nc = c + dc[dir];

				if (nr < 0 || nr >= n || nc < 0 || nc >= n || arr[nr][nc] != 0) {
					dir = (dir + 1) % 4;
					continue;
				}
				arr[nr][nc] = cnt++;
				r = nr;
				c = nc;
			}
			
			System.out.printf("#%d\n", test_case);
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					System.out.printf("%d ", arr[i][j]);
				}
				System.out.println();
			}

		}

	}

}
