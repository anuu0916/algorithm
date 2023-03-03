package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_1949_모의_등산로조성_안유진 {
	static int N, K, ans;
	static int[][] map;
	static boolean[][] visited;
	static int top;
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			// test case마다 초기화
			ans = 0;
			top = 0;
			
			stk = new StringTokenizer(br.readLine());
			N = Integer.parseInt(stk.nextToken());
			K = Integer.parseInt(stk.nextToken());
			
			map = new int[N][N];
			for (int i = 0; i < N; i++) {
				stk = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(stk.nextToken());
					top = Math.max(top, map[i][j]); // 가장 높은 봉우리 찾기
				}
			}
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					// 가장 높은 봉우리를 만나면 등산로 찾기
					if (map[i][j] == top) {
						visited = new boolean[N][N];
						visited[i][j] = true;
						getTrail(i, j, map[i][j], 1, false);
					}
				}
			}
			
			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		}
		
		System.out.print(sb);
	}
	
	/**
	 * @param r 		현재 row값
	 * @param c 		현재 column값
	 * @param height	현재 있는 곳의 높이
	 * @param len		지금까지 온 등산로의 길이
	 * @param cutoff	공사 여부
	 */
	private static void getTrail(int r, int c, int height, int len, boolean cutoff) {
		ans = Math.max(ans, len);
		
		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			
			if (nr < 0 || nr >= N || nc < 0 || nc >= N || visited[nr][nc]) continue;
			if (map[nr][nc] >= height) {
				// 이미 공사를 했거나 최대 깊이만큼 깎아도 가지 못할 경우
				if (cutoff || map[nr][nc] - K >= height) continue;
				else {
					// 공사가 가능한 경우
					visited[nr][nc] = true;
					getTrail(nr, nc, height - 1, len+1, true);
					visited[nr][nc] = false;
				}
			} else {
				// 공사를 하지 않아도 되는 경우
				visited[nr][nc] = true;
				getTrail(nr, nc, map[nr][nc], len+1, cutoff);
				visited[nr][nc] = false;
				
			}
		}
		
	}

}
 