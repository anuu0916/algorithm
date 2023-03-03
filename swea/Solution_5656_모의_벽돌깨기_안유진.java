package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution_5656_모의_벽돌깨기_안유진 {
	static int N, W, H;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int res = Integer.MAX_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringTokenizer stk;
		StringBuilder sb = new StringBuilder();

		int[][] map;

		for (int tc = 1; tc < T + 1; tc++) {
			stk = new StringTokenizer(br.readLine());
			N = Integer.parseInt(stk.nextToken());
			W = Integer.parseInt(stk.nextToken());
			H = Integer.parseInt(stk.nextToken());
			
			res = Integer.MAX_VALUE;
			map = new int[H][W];
			for (int i = 0; i < H; i++) {
				stk = new StringTokenizer(br.readLine());
				for (int j = 0; j < W; j++) {
					map[i][j] = Integer.parseInt(stk.nextToken());
				}
			}

			throwBall(map, 0);
			
			sb.append("#").append(tc).append(" ").append(res).append("\n");
		}
		
		System.out.print(sb);
		
	}
	
	// 구슬 한 번 던지기
	private static boolean throwBall(int[][] map, int cnt) {
		if (cnt == N) {
			int min = Math.min(res, count(map)); 
			if (res > min) res = min;
			return false;
		}
		
		// 최적의 해를 찾았으면 상태공간트리 다 돌지 않고 끝내기
		if (count(map) == 0) {
			res = 0;
			return true;
		}
		
		int r = 0;
		int[][] copied = new int[H][W];
		for (int c = 0; c < W; c++) {
			r = 0;
			while (r < H && map[r][c] == 0)
				r++;

			if (r == H)
				continue;
			
			// 복사
			copy(map, copied);
			
			// 벽돌 제거
			remove(copied, r, c);

			// 벽돌 밑으로 떨어뜨리기
			down(copied);

			if(throwBall(copied, cnt + 1)) return true;
			
		}
		return false;

	}
	
	private static void copy(int[][] map, int[][] copied) {
		for (int j = 0; j < H; j++) {
			for (int k = 0; k < W; k++) {
				copied[j][k] = map[j][k];
			}
		}
	}
	
	private static int count(int[][] map) {
		int brick = 0;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (map[i][j] > 0)
					brick++;
			}
		}
		
		return brick;
	}

	private static void down(int[][] map) {
		Deque<Integer> stack = new ArrayDeque<>();
		
		for (int c = 0; c < W; c++) {
			for (int r = 0; r < H; r++) {
				if (map[r][c] > 0) {
					stack.offerLast(map[r][c]);
					map[r][c] = 0;
				}
			}
			
			int r = H-1;
			while(!stack.isEmpty()) {
				map[r--][c] = stack.pollLast();
			}
		}
	}

	private static void remove(int[][] map, int r, int c) {

		Queue<int[]> queue = new ArrayDeque<int[]>();
		if (map[r][c] > 1) {
			queue.offer(new int[] { r, c, map[r][c] - 1 });
		}
		map[r][c] = 0;

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int len = cur[2];

			int nr, nc;
			for (int i = 0; i < 4; i++) {
				for (int j = 1; j <= len; j++) {
					nr = cur[0] + dr[i] * j;
					nc = cur[1] + dc[i] * j;

					if (nr < 0 || nr >= H || nc < 0 || nc >= W)
						continue;
					if (map[nr][nc] == 0)
						continue;

					queue.offer(new int[] { nr, nc, map[nr][nc] - 1});
					map[nr][nc] = 0;
				}
			}
		}
	}

}
