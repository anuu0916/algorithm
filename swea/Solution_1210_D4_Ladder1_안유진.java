package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_1210_D4_Ladder1_안유진 {	
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder(10);
		int case_num;
		String[][] map = new String[100][];
		
		int goal = -1;
		
		for (int test_case = 1; test_case < 11; test_case++) {
			case_num = Integer.parseInt(br.readLine());
			int[][] visited = new int[100][100];
			
			for (int i = 0; i < 100; i++) {
				String[] tmp = br.readLine().split(" ");
				map[i] = tmp;
			}
			
			for (int i = 0; i < 100; i++) {
				if (map[99][i].equals("2")) {
					goal = i;
					break;
				}
			}
			
			int curR = 99;
			int curC = goal;
			visited[curR][curC] = 1;
			while (curR > 0) {
//				System.out.println(curR +", "+curC);
				if (curC+1 < 100 && visited[curR][curC+1] == 0 && map[curR][curC+1].equals("1")) {
					visited[curR][++curC] = 1;
				}
				else if (curC-1 > -1 && visited[curR][curC-1] == 0 && map[curR][curC-1].equals("1")) {
					visited[curR][--curC] = 1;
				}
				else {
					visited[--curR][curC] = 1;
				}
			}
			
			sb.append(String.format("#%d %d\n", case_num, curC));
			
		}
		
		System.out.println(sb.toString());

	}

}
