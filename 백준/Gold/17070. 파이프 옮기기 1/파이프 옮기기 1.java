import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static class Pos {
		int r1, c1, r2, c2;

		public Pos(int r1, int c1, int r2, int c2) {
			super();
			this.r1 = r1;
			this.c1 = c1;
			this.r2 = r2;
			this.c2 = c2;
		}
		
		private int whichShape() {
			int shape = 0;
			int rd = r2 - r1;
			int cd = c2 - c1;
			
			if (rd == 0 && cd == 1) { // 가로
				shape = HOR;
			} else if (rd == 1 && cd == 0) { // 세로
				shape = VER;
			} else if (rd == 1 && cd == 1) { // 대각선
				shape = DIA;
			}
			
			return shape;
		}
		
	}

	static final int HOR = 1;
	static final int VER = 2;
	static final int DIA = 3;
	

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[][] map = new int[N][N];
		StringTokenizer stk;
		
		
		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(stk.nextToken());
			}
		}
		
		int cnt = 0;
		Queue<Pos> queue = new ArrayDeque<Pos>();
		
		queue.offer(new Pos(0,0,0,1));
		
		int r1, c1, r2, c2; // 현재 위치
		int sr, sc, er, ec; // 새로운 위치
		int shape; // 모양
		while(!queue.isEmpty()) {
			Pos cur = queue.poll();
			shape = cur.whichShape();
			r1 = cur.r1;
			c1 = cur.c1;
			r2 = cur.r2;
			c2 = cur.c2;
			
			if (r2 == N-1 && c2 == N-1) {
				cnt++;
				continue;
			}
			
			// 오른쪽으로 밀기
			if (shape != VER) {
				er = r2;
				ec = c2 + 1;
				
				if (ec < N && map[er][ec] == 0) {
					queue.offer(new Pos(r2, c2, er, ec));
				}
			}
			
			// 대각선으로 밀기
			er = r2+1;
			ec = c2+1;
			if (er < N && ec < N && 
					map[er][ec] == 0 && map[er-1][ec] == 0 && map[er][ec-1] == 0) {
				queue.offer(new Pos(r2, c2, er, ec));
			}
			
			// 아래로 밀기
			if (shape != HOR) {
				er = r2 + 1;
				ec = c2;
				
				if (er < N && map[er][ec] == 0) {
					queue.offer(new Pos(r2, c2, er, ec));
				}
			}
		}
		
		System.out.println(cnt);
		
	}

}