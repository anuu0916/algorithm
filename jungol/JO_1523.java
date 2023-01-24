package kr.co.jungol.beginner;

import java.util.Scanner;

public class JO_1523 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		if (n < 0 || n > 100 || m < 1 || m > 3) {
			System.out.println("INPUT ERROR!");
			return;
		}

		if (m == 1) {
			for (int i = 1; i < n + 1; i++) {
				for (int j = 0; j < i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
		} else if (m == 2) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n - i; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
		} else if (m == 3) {
			for (int i = 0; i < n; i++) {
				for (int j = 1; j < n-i; j++) {
					System.out.print(" ");
				}
				for (int j = 0; j < 2*i+1; j++) {
					System.out.print("*");
				}
				System.out.println();
			}
		}

	}

}
