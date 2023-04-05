import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static class Pos {
		int x, y;

		public Pos(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}

		@Override
		public String toString() {
			return "Pos [x=" + x + ", y=" + y + "]";
		}
	}

	static int N;
	static Pos home, adj[], fest;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine()) + 1;

			// 집 좌표 입력
			stk = new StringTokenizer(br.readLine());
			home = new Pos(Integer.parseInt(stk.nextToken()), Integer.parseInt(stk.nextToken()));

			// 편의점 좌표 입력
			adj = new Pos[N];
			for (int i = 0; i < N; i++) {
				stk = new StringTokenizer(br.readLine());
				adj[i] = new Pos(Integer.parseInt(stk.nextToken()), Integer.parseInt(stk.nextToken()));
			}

			fest = adj[N-1];
			
			Queue<Pos> queue = new ArrayDeque<Pos>();
			boolean[] visited = new boolean[N+1];
			boolean flag = false;
			queue.add(home);
			
			Pos cur;
			while(!queue.isEmpty()) {
				cur = queue.poll();
				
				for (int i = 0; i < N; i++) {
					if (!visited[i] && getDist(cur.x, cur.y, adj[i].x, adj[i].y) <= 1000) {
						if (adj[i].x == fest.x && adj[i].y == fest.y) {
							flag = true;
							break;
						}
						
						queue.add(adj[i]);
						visited[i] = true;
					}
				}
				
			}
			if (flag) sb.append("happy").append("\n");
			else sb.append("sad").append("\n");
		}
		

		System.out.print(sb);
	}

	private static int getDist(int cx, int cy, int nx, int ny) {
		return Math.abs(nx - cx) + Math.abs(ny - cy);
	}

}