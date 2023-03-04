import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

/*
 * 1. 상어를 객체로 입력받기
 * 2. 상어를 잡고
 * 3. 상어 이동시키기
 * 4. 같은 칸에 있는지 확인하고 상어 잡아먹기 
 */

public class Main {
	private static class Shark {
		int r, c; // 위치
		int s; // 속력
		int d; // 이동 방향
		int z; // 크기
		boolean isKilled = false;

		public Shark(int r, int c, int s, int d, int z) {
			super();
			this.r = r;
			this.c = c;
			this.s = s;
			this.d = d;
			this.z = z;
		}

		@Override
		public String toString() {
			StringBuilder builder = new StringBuilder();
			builder.append("Shark [r=").append(r).append(", c=").append(c).append(", 속력=").append(s).append(", 이동방향=")
					.append(d).append(", 크기=").append(z).append(", 죽음=").append(isKilled).append("]");
			return builder.toString();
		}

	}

	static int R, C; // 격자판의 크기
	static int M; // 상어의 수
	static int res; // 낚시왕이 잡은 상어 크기의 합
	static Shark[] sharkList;
	static int[][] map;
	// 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
	static int[] dr = { 0, -1, 1, 0, 0 };
	static int[] dc = { 0, 0, 0, 1, -1 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());

		R = Integer.parseInt(stk.nextToken());
		C = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());

		map = new int[R + 1][C + 1];
		sharkList = new Shark[M+1];
		
		sharkList[0] = new Shark(0, 0, 0, 0, 0);
		int r, c, s, d, z;
		for (int i = 1; i < M+1; i++) {
			stk = new StringTokenizer(br.readLine());
			r = Integer.parseInt(stk.nextToken());
			c = Integer.parseInt(stk.nextToken());
			s = Integer.parseInt(stk.nextToken());
			d = Integer.parseInt(stk.nextToken());
			z = Integer.parseInt(stk.nextToken());

			// 위, 아래 이동일 경우
			if (d < 3) {
				s %= (R - 1) * 2;
			} else { // 왼쪽, 오른쪽 이동일 경우
				s %= (C - 1) * 2;
			}
			sharkList[i] = new Shark(r, c, s, d, z);
		}
		
		Arrays.sort(sharkList, (o1, o2) -> {return o1.z - o2.z;});
		
		for (int i = 1; i < M+1; i++) {
			map[sharkList[i].r][sharkList[i].c] = i;
		}

		for (int i = 1; i < C + 1; i++) {
			// 상어 잡기
			catchShark(i);

			// 상어 이동
			move();
		}

		System.out.println(res);
	}

	private static void catchShark(int col) {
		int idx = -1;
		int i;

		for (i = 1; i < R + 1; i++) {
			if (map[i][col] > 0) {
				idx = map[i][col];
				break;
			}
		}

		if (idx == -1)
			return;

		map[i][col] = 0;
		res += sharkList[idx].z;
		sharkList[idx].isKilled = true;
	}

	private static void move() {
		int speed, dir;
		int cr, cc;
		int[][] newMap = new int[R+1][C+1];
		
		Shark cur;
		for (int i = M; i > 0; i--) {
			cur = sharkList[i];
			if (cur.isKilled)
				continue;

			dir = cur.d;
			speed = cur.s;
			cr = cur.r;
			cc = cur.c;

			for (int j = 0; j < speed; j++) {
				cr += dr[dir];
				cc += dc[dir];

				if (cr < 1) {
					cr = 2;
					dir = turn(dir);
				}
				if (cr > R) {
					cr = R - 1;
					dir = turn(dir);
				}
				if (cc < 1) {
					cc = 2;
					dir = turn(dir);
				}
				if (cc > C) {
					cc = C - 1;
					dir = turn(dir);
				}
			}

			if (newMap[cr][cc] > 0) {
				sharkList[i].isKilled = true;
				continue;
			} else {
				newMap[cr][cc] = i;
			}

			cur.r = cr;
			cur.c = cc;
			cur.d = dir;

		}
		
		map = newMap;
	}

	private static int turn(int dir) {
		int nd = 0;

		if (dir == 1)
			nd = 2;
		else if (dir == 2)
			nd = 1;
		else if (dir == 3)
			nd = 4;
		else if (dir == 4)
			nd = 3;

		return nd;
	}

}