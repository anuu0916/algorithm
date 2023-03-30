import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	static int[][] map = new int[9][9];
	static boolean[][] row = new boolean[9][10];
	static boolean[][] col = new boolean[9][10];
	static boolean[][] sqr = new boolean[9][10];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String tmp;
		for (int i = 0; i < 9; i++) {
			tmp = br.readLine();
			for (int j = 0; j < 9; j++) {
				map[i][j] = tmp.charAt(j) - '0';
				if (map[i][j] != 0) {
					row[i][map[i][j]] = true;
					col[j][map[i][j]] = true;
					sqr[(i/3)*3 + (j/3)][map[i][j]] = true;
				}
			}
		}

		dfs(0);

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				sb.append(map[i][j]);
			}
			sb.append("\n");
		}
		System.out.print(sb);
	}

	private static boolean dfs(int cnt) {
		int r = cnt / 9;
		int c = cnt % 9;
		if (cnt == 81) {
			return true;
		}

		if (map[r][c] != 0) {
			if (dfs(cnt + 1))
				return true;
		} else {
			for (int i = 1; i <= 9; i++) {
				if (row[r][i] || col[c][i] || sqr[(r/3)*3 + (c/3)][i])
					continue;
				
				row[r][i] = true;
				col[c][i] = true;
				sqr[(r/3)*3 + (c/3)][i] = true;
				
				map[r][c] = i;
				if (dfs(cnt+1)) return true;
				map[r][c] = 0;
				
				row[r][i] = false;
				col[c][i] = false;
				sqr[(r/3)*3 + (c/3)][i] = false;
			}
		}

		return false;
	}

}