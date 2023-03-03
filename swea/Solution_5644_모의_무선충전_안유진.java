package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

class BC {
	int x, y, c, p;
	public BC() {}
	
}

public class Solution_5644_모의_무선충전_안유진 {
	static int M;
	static int A;
	static int[] dy = {0, -1, 0, 1, 0};
	static int[] dx = {0, 0, 1, 0, -1};
	static BC[] bcs;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			stk = new StringTokenizer(br.readLine());
			M = Integer.parseInt(stk.nextToken());
			A = Integer.parseInt(stk.nextToken());
			
			int[] moveA = new int[M];
			stk = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				moveA[i] = Integer.parseInt(stk.nextToken());
			}
			
			int[] moveB = new int[M];
			stk = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				moveB[i] = Integer.parseInt(stk.nextToken());
			}
			
			bcs = new BC[A];
			for (int i = 0; i < A; i++) {
				bcs[i] = new BC();
				stk = new StringTokenizer(br.readLine());
				bcs[i].x = Integer.parseInt(stk.nextToken());
				bcs[i].y = Integer.parseInt(stk.nextToken());
				bcs[i].c = Integer.parseInt(stk.nextToken());
				bcs[i].p = Integer.parseInt(stk.nextToken());
			}
			
			Arrays.sort(bcs, new Comparator<BC>() {

				@Override
				public int compare(BC o1, BC o2) {
					return o2.p - o1.p;
				}
			});
			
			int ay = 1, ax = 1;
			int by = 10, bx = 10;
			int sum = getMaxCharge(ay, ax, by, bx);
			for (int i = 0; i < M; i++) {
				ay += dy[moveA[i]];
				ax += dx[moveA[i]];
				by += dy[moveB[i]];
				bx += dx[moveB[i]];
				
				sum += getMaxCharge(ay, ax, by, bx);
				
			}
			
			sb.append("#").append(tc).append(" ").append(sum).append("\n");
		}
		
		System.out.print(sb);

	}
	
	private static int charge(int i, int y, int x) {
		if (Math.abs(y - bcs[i].y) + Math.abs(x - bcs[i].x) <= bcs[i].c) {
			return bcs[i].p;
		}
		return 0;
	}

	private static int getMaxCharge(int ay, int ax, int by, int bx) {
		int max = 0;
		for (int i = 0; i < A; i++) {
			int chargeA = charge(i, ay, ax);
			int sum = 0;
			for (int j = 0; j < A; j++) {
				int chargeB = charge(j, by, bx);
				if (i == j) {
					sum = Math.max(chargeA, chargeB);
				} else {
					sum = chargeA + chargeB;
				}
				
				max = Math.max(max, sum);
			}
		}
		return max;
	}
	
	

}
