package kr.co.jungol.beginner;

import java.util.Scanner;

public class JO_1329 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		if (n < 0 || n > 100 || n % 2 == 0) {
			System.out.println("INPUT ERROR!");
			return;
		}

		for (int i = 1; i < n / 2 + 2; i++) {
			for (int j = 1; j < i; j++) {
				System.out.print(" ");
			}
			for (int j = 1; j < 2 * i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
		for (int i = n / 2; i > 0; i--) {
			for (int j = 1; j < i; j++) {
				System.out.print(" ");
			}
			for (int j = 1; j < 2 * i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}
