package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;

public class Solution_1873_D3_상호의배틀필드_안유진 {
	static int H, W, N;
	static char[][] map;
	static HashMap<Character, int[]> move = new HashMap<>();
	static HashMap<Character, Character> dir = new HashMap<>();
	static int ch, cw;
	static char cdir;
	static String cmd; 
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		
		move.put('U', new int[] {-1, 0});
		move.put('D', new int[] {1, 0});
		move.put('L', new int[] {0, -1});
		move.put('R', new int[] {0, 1});
		
		dir.put('^', 'U');
		dir.put('v', 'D');
		dir.put('<', 'L');
		dir.put('>', 'R');
		
		for (int tc = 1; tc <= T; tc++) {
			String[] line = br.readLine().split(" ");
			H = Integer.parseInt(line[0]);
			W = Integer.parseInt(line[1]);
			
			map = new char[H][W];
			
			for (int i = 0; i < H; i++) {
				String tmp = br.readLine();
				for (int j = 0; j < W; j++) {
					map[i][j] = tmp.charAt(j);
					if (dir.containsKey(map[i][j])) {
						ch = i;
						cw = j;
						cdir = dir.get(map[i][j]);
						map[i][j] = '.';
					}
				}
			}
			
			N = Integer.parseInt(br.readLine());
			cmd = br.readLine();
			
			for (int i = 0; i < N; i++) {
				char cur_cmd = cmd.charAt(i);
				if (cur_cmd == 'S') shoot(ch, cw);
				else {
					cdir = cur_cmd;
					move_tank();
					
				}
			}
			
			if (cdir == 'U') map[ch][cw] = '^';
			else if (cdir == 'D') map[ch][cw] = 'v';
			else if (cdir == 'L') map[ch][cw] = '<';
			else if (cdir == 'R') map[ch][cw] = '>';
			
			sb.append("#").append(tc).append(" ");
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					sb.append(map[i][j]);
				}
				sb.append("\n");
			}
			
			
		}
		
		System.out.print(sb);
	}

	private static void move_tank() {
		int nh = ch + move.get(cdir)[0];
		int nw = cw + move.get(cdir)[1];
		
		if (nh < 0 || nh >= H || nw < 0 || nw >= W) return;
		if (map[nh][nw] != '.') return;
		
		ch = nh;
		cw = nw;
	}

	private static void shoot(int h, int w) {
		while (h > -1 && h < H && w > -1 && w < W) {
			if (map[h][w] == '*') {
				map[h][w] = '.';
				break;
			} else if (map[h][w] == '#') {
				break;
			}
			
			h += move.get(cdir)[0];
			w += move.get(cdir)[1];
		}
	}

}
