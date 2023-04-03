import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
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

		@Override
		public String toString() {
			return "Pos [r=" + r + ", c=" + c + "]";
		}
		
		
		
	}
	static int R, C;
	static char[][] map;
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		R = Integer.parseInt(stk.nextToken());
		C = Integer.parseInt(stk.nextToken());
		
		map = new char[R][C];
		
		
		Queue<Pos> queue = new ArrayDeque<>();
		
		String tmp;
		for (int i = 0; i < R; i++) {
			tmp = br.readLine();
			for (int j = 0; j < C; j++) {
				map[i][j] = tmp.charAt(j);
				if (map[i][j] == 'S') {
					queue.add(new Pos(i, j));
					map[i][j] = '-';
				}
			}
		}
		
		Pos cur;
		int cnt = 0;
		int nr, nc;
		boolean flag = false;
		
		p1 : 
		while(!queue.isEmpty()) {
			flood();
			
			
			cnt++;
			for (int i = 0, size = queue.size(); i < size; i++) {
				cur = queue.poll();
				
				for (int j = 0; j < 4; j++) {
					nr = cur.r + dr[j];
					nc = cur.c + dc[j];
					
					if (!isValid(nr, nc) || map[nr][nc] == '-') continue;
					
					if (map[nr][nc] == 'D') {
						flag = true;
						break p1;
					}
					
					queue.add(new Pos(nr, nc));
					map[nr][nc] = '-';
					
				}
			}

		}
		
		if (flag) System.out.println(cnt);
		else System.out.println("KAKTUS");
		
	}

	private static void flood() {
		boolean[][] visited = new boolean[R][C];
		
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (visited[i][j]) continue;
				
				if (map[i][j] == '*') {
					visited[i][j] = true;
					
					for (int k = 0; k < 4; k++) {
						int nr = i + dr[k];
						int nc = j + dc[k];
						
						if (!isValid(nr, nc) || map[nr][nc] == 'D') continue;
						
						map[nr][nc] = '*';
						visited[nr][nc] = true;
					}
				}
			}
		}
	}

	private static boolean isValid(int nr, int nc) {
		if (nr < 0 || nr >= R || nc < 0 || nc >= C) return false;
		if (map[nr][nc] == 'X' || map[nr][nc] == '*') return false;
		return true;
	}

}