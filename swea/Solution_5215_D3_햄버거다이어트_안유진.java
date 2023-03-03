package swea;

import java.util.Scanner;

public class Solution_5215_D3_햄버거다이어트_안유진 {
	static int N, L;
	static int res;
	static int[][] arr;
	static int[] numbers;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			N = sc.nextInt();
			L = sc.nextInt();
			arr = new int[N][2];
			
			for (int i = 0; i < N; i++) {
				arr[i][0] = sc.nextInt();
				arr[i][1] = sc.nextInt();
			}
			
			res = 0;
			combi(0, 0, 0);
			
			System.out.printf("#%d %d\n", test_case, res);
		}

	}

	private static void combi(int cnt, int cal, int score) {
		if (cal > L) return;
		
		if (cnt == N) {
			res = Math.max(res, score);
			return;
		}
		
		combi(cnt+1, cal+arr[cnt][1], score+arr[cnt][0]);
		
		combi(cnt+1, cal, score);
	}
	
	

}
