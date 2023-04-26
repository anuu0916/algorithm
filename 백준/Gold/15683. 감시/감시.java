import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static List<int[]> cctvList;
	static int N, M;
	static int tvNum = 0, answer = Integer.MAX_VALUE;
	// 상 우 하 좌
	static int[] dr = { -1, 0, 1, 0 };
	static int[] dc = { 0, 1, 0, -1 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());

		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());

		int[][] map = new int[N][M];
		cctvList = new ArrayList<int[]>();

		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(stk.nextToken());
				if (isCCTV(map[i][j])) {
					cctvList.add(new int[] { i, j });
				}
			}
		}

		tvNum = cctvList.size();
		
		dfs(0, map);

		System.out.println(answer);
	}

	private static void dfs(int cnt, int[][] map) {
		if (cnt == tvNum) {
			answer = Math.min(answer, getBlind(map));
			return;
		}

		int i = cctvList.get(cnt)[0];
		int j = cctvList.get(cnt)[1];
		
		int[][] tmp = new int[N][M];

		for (int d = 0; d < 4; d++) {
			copyMap(map, tmp);
			switch (map[i][j]) {
			case 1:
				fill(tmp, i, j, d, -1);
				dfs(cnt + 1, tmp);
				break;
			case 2:
				if (d > 1) break;
				fill(tmp, i, j, d, -1);
				fill(tmp, i, j, (d + 2) % 4, -1);
				dfs(cnt + 1, tmp);
				break;
			case 3:
				fill(tmp, i, j, d, -1);
				fill(tmp, i, j, (d + 1) % 4, -1);
				dfs(cnt + 1, tmp);
				break;
			case 4:
				fill(tmp, i, j, d, -1);
				fill(tmp, i, j, (d + 1) % 4, -1);
				fill(tmp, i, j, (d + 2) % 4, -1);
				dfs(cnt + 1, tmp);
				break;
			case 5:
				if (d > 0) break;
				fill(tmp, i, j, d, -1);
				fill(tmp, i, j, (d + 1) % 4, -1);
				fill(tmp, i, j, (d + 2) % 4, -1);
				fill(tmp, i, j, (d + 3) % 4, -1);
				dfs(cnt + 1, tmp);
				break;
			}
		}
		return;
	}


	private static void copyMap(int[][] origin, int[][] copied) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				copied[i][j] = origin[i][j];
			}
		}
	}

	private static void fill(int[][] map, int row, int col, int d, int val) {
		row += dr[d];
		col += dc[d];
		while (row > -1 && row < N && col > -1 && col < M) {
			if (map[row][col] == 6)
				break;
			
			if (!isCCTV(map[row][col])) {
				map[row][col] = val;
			}
			row += dr[d];
			col += dc[d];
		}

	}

	private static boolean isCCTV(int num) {
		if (num > 0 && num < 6) return true;
		return false;
	}

	private static int getBlind(int[][] map) {
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 0)
					cnt++;

			}
		}

		return cnt;
	}

}