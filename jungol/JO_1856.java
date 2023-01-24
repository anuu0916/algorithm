package kr.co.jungol.beginner;

import java.util.Scanner;

public class JO_1856 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();

		StringBuilder sb = new StringBuilder();
		int num = 1;
		for (int i = 0; i < n; i++) {
			sb.setLength(0);
			if(i%2 == 0) {
				for (int j = 0; j < m; j++) {
					sb.append(num+j).append(" ");
				}
			} else {
				for (int j = m-1; j > -1; j--) {
					sb.append(num+j).append(" ");
				}
			}
			System.out.println(sb.toString());
			num += m;
		}

	}

}
