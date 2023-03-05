import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N = 10;
	static int res = 100;
	static int[] num = { 0, 5, 5, 5, 5, 5 };
	static int[][] map = new int[N][N];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		int cnt = 0;

		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(stk.nextToken());
				if (map[i][j] == 1)
					cnt++;
			}
		}

		if (cnt == 0) {
			System.out.println(0);
			return;
		}

		paper(cnt, 0);

		if (res == 100)
			System.out.println(-1);
		else
			System.out.println(res);

	}

	private static void paper(int cnt, int use) {

		if (res < use)
			return;

		if (cnt == 0) {
			res = Math.min(res, use);
			return;
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (map[i][j] == 0) continue;
				
				for (int size = 1; size < 6; size++) {
					if (i + size <= N && j + size <= N) {
						if (num[size] > 0 && check(i, j, size)) {
							// 덮는 경우
							fill(i, j, size, 0);
							num[size]--;
							paper(cnt - (size * size), use + 1);

							// 덮지 않는 경우
							fill(i, j, size, 1);
							num[size]++;
							
						}
					}
				}
				return;
			}
		}
	}

	private static void fill(int sr, int sc, int size, int value) {
		for (int i = sr; i < sr + size; i++) {
			for (int j = sc; j < sc + size; j++) {
				map[i][j] = value;
			}
		}
	}

	private static boolean check(int sr, int sc, int size) {
		// 색종이 크기만큼 전부 1인지 체크
		for (int i = sr; i < sr + size; i++) {
			for (int j = sc; j < sc + size; j++) {
				if (map[i][j] == 0)
					return false;
			}
		}

		return true;

	}

}