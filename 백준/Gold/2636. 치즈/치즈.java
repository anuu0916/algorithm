import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static class Pos{
		int r, c;

		public Pos(int r, int c) {
			super();
			this.r = r;
			this.c = c;
		}
		
	}
	
	static int H, W;
	static int[][] map;
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		H = Integer.parseInt(stk.nextToken());
		W = Integer.parseInt(stk.nextToken());
		
		map = new int[H][W];
		
		int before = 0;
		for (int i = 0; i < H; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < W; j++) {
				map[i][j] = Integer.parseInt(stk.nextToken());
				if (map[i][j] == 1) before++; 
			}
		}
		
		
		int time = 0;
		int after = 0;
		while(true) {
			bfs();
			time++;
			
			after = cnt_cheese();
			if (after == 0) break;
			else before = after;
		}
		
		System.out.println(time);
		System.out.println(before);
	}
	
	private static void bfs() {
		int[][] tmp = new int[H][W];
		copy(tmp);
		
		Queue<Pos> queue = new ArrayDeque<Pos>();
		queue.offer(new Pos(0, 0));
		map[0][0] = -1;
		
		Pos cur;
		int nr, nc;
		while(!queue.isEmpty()) {
			cur = queue.poll();
			
			for (int i = 0; i < 4; i++) {
				nr = cur.r + dr[i];
				nc = cur.c + dc[i];
				
				if (nr < 0 || nr >= H || nc < 0 || nc >= W || map[nr][nc] == -1) continue;
				
				
				if (map[nr][nc] == 1) {
					tmp[nr][nc] = 0;
				} else {
					queue.offer(new Pos(nr, nc));
				}
				
				map[nr][nc] = -1;
				
			}
		}
		
		map = tmp;
		
	}
	
	
	private static void copy(int[][] tmp) {
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				tmp[i][j] = map[i][j];
			}
		}
	}

	private static int cnt_cheese() {
		int cnt = 0;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (map[i][j] == 1) cnt++;
			}
		}
		
		return cnt;
	}

}