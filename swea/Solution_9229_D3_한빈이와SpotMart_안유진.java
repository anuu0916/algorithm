package swea;

import java.util.Scanner;

public class Solution_9229_D3_한빈이와SpotMart_안유진 {
	static int N, M;
	static int[] snack;
	static int MAX;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		
		for (int test_case = 1; test_case <= TC; test_case++) {
			N = sc.nextInt();
			M = sc.nextInt();
			snack = new int[N];
			
			MAX = -1;
			
			for (int i = 0; i < N; i++) {
				snack[i] = sc.nextInt();
			}
			
			combi(0, 0, 0);
			
			System.out.printf("#%d %d\n", test_case, MAX);
			
		}
		
	}
	
	private static void combi(int cnt, int start, int sum) {
		if (cnt == 2) {
			if (sum <= M && sum > MAX) {
				MAX = sum;
			}
			return;
		}
		
		if (sum > M) return;
		
		for (int i = start; i < N; i++) {
			combi(cnt+1, i+1, sum + snack[i]);
		}
	}

}
