import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N = 4, res = 0;
	
	// 반시계 회전
	// ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
	static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1};
	static int[] dc = {0, -1, -1, -1, 0, 1, 1, 1};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		
		int num=0, dir=0, sdir=0;
		int[][][] map = new int[N][N][2];
		
		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				num = Integer.parseInt(stk.nextToken());
				dir = Integer.parseInt(stk.nextToken()) - 1;
				
				map[i][j][0] = num;
				map[i][j][1] = dir;
				if (i ==0 && j == 0) {
					sdir = dir;
					map[i][j][0] = 0;
					res += num;
				}
				
			}
		}
		
		int[][][] tmp = new int[N][N][2];
		copyMap(map, tmp);
		dfs(0, 0, sdir, tmp, res);
		
		System.out.println(res);
	}

	private static void dfs(int sr, int sc, int sdir, int[][][] map, int sum) {
		res = Math.max(res, sum);
		
		moveFish(sr, sc, map);
		
		int[][][] tmp = new int[N][N][2];
		int nr = sr, nc = sc;
		for (int i = 1; i < N; i++) {
			nr += dr[sdir];
			nc += dc[sdir];
			
			if (!isValid(nr, nc)) break;
			if (map[nr][nc][0] == 0) continue;
			
			copyMap(map, tmp);
			tmp[sr][sc][0] = 0;
			tmp[nr][nc][0] = -1;
			
			dfs(nr, nc, map[nr][nc][1], tmp, sum + map[nr][nc][0]);
		}
	}

	private static void copyMap(int[][][] origin, int[][][] copy) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				copy[i][j][0] = origin[i][j][0];
				copy[i][j][1] = origin[i][j][1];
			}
		}
	}
    
	private static void moveFish(int sr, int sc, int[][][] map) {
		int nr, nc, ndir, dir;
		
		int[] idx = new int[2];
		for (int i = 1; i < N*N+1; i++) {
			idx = findFish(i, map);
			if (idx[0] == -1 && idx[1] == -1) continue;
			
			dir = map[idx[0]][idx[1]][1];
			for (int j = 0; j < 8; j++) {
				ndir = (dir + j) % 8;
				nr = idx[0] + dr[ndir];
				nc = idx[1] + dc[ndir];
				
				if (!isValid(nr, nc) || (nr == sr && nc == sc)) continue;
				
				if (map[nr][nc][0] == 0) {
					map[idx[0]][idx[1]][0] = 0; 
					map[nr][nc][0] = i;
					map[nr][nc][1] = ndir;
					
				} else {
					swap(idx[0], idx[1], ndir, nr, nc, map);
				}
				
				break;
			}
			
		}
	}

	private static void swap(int i, int j, int dir, int nr, int nc, int[][][] map) {
		int num = map[i][j][0];
		
		map[i][j][0] = map[nr][nc][0];
		map[i][j][1] = map[nr][nc][1];
		
		map[nr][nc][0] = num;
		map[nr][nc][1] = dir;
	}

	private static int[] findFish(int num, int[][][] map) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (map[i][j][0] == num) {
					return new int[] {i, j};
				}
			}
		}
		return new int[] {-1, -1};
	}

	private static boolean isValid(int nr, int nc) {
		if (nr < 0 || nr >= N || nc < 0 || nc >= N) return false;
		return true;
	}

}