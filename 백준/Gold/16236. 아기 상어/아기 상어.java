import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] map;
	static int sr, sc; // 상어의 위치
	static int size = 2; // 상어의 크기
	static int eat = 0; // 먹은 물고기 수
	static int[] dr = { -1, 0, 1, 0 };
	static int[] dc = { 0, -1, 0, 1 };
	static int cnt; // 걸린 시간

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new int[N][N];

		StringTokenizer stk;
		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(stk.nextToken());

				if (map[i][j] == 9) {
					sr = i;
					sc = j;
					map[i][j] = 0;
				}
			}
		}

		while (getFish()) {
			if (size == eat) {
				size++;
				eat = 0;
			}
		}

		System.out.println(cnt);

	}

	private static boolean getFish() {
		Queue<int[]> queue = new ArrayDeque<int[]>();
		queue.offer(new int[] { sr, sc, 0 });

		boolean[][] visited = new boolean[N][N];
		visited[sr][sc] = true;

		int fr = N + 1, fc = N + 1, move = Integer.MAX_VALUE;
		while (!queue.isEmpty()) {
			int[] cur = queue.poll();

			if (map[cur[0]][cur[1]] > 0 && map[cur[0]][cur[1]] < size) {
				if (move > cur[2]) {
					fr = cur[0];
					fc = cur[1];
					move = cur[2];
				} else if (move == cur[2]) {
					if (fr > cur[0]) {
						fr = cur[0];
						fc = cur[1];
					} else if (fr == cur[0] && fc > cur[1]) {
						fc = cur[1];
					}
				}
			}

			for (int i = 0; i < 4; i++) {
				int nr = cur[0] + dr[i];
				int nc = cur[1] + dc[i];

				// 범위 검사
				if (nr < 0 || nr >= N || nc < 0 || nc >= N)
					continue;

				// 방문했거나 상어보다 큰 물고기가 있는 칸은 지나갈 수 없음
				if (visited[nr][nc] || map[nr][nc] > size)
					continue;

				visited[nr][nc] = true;
				queue.offer(new int[] { nr, nc, cur[2] + 1 });
			}
		}

		if (move == Integer.MAX_VALUE)
			return false;

		map[fr][fc] = 0;
		eat++;
		sr = fr;
		sc = fc;
		cnt += move;

		return true;
	}

}