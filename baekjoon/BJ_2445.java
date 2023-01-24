package net.acmicpc.problem;

import java.util.Scanner;

public class BJ_2445 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int i, j;
		for (i = 1; i < n+1; i++) {
			for (j = 0; j < i; j++) {
				System.out.print("*");
			}
			for (j = 0; j < 2*(n-i); j++) {
				System.out.print(" ");
			}
			for (j = 0; j < i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
		for (i = n-1; i > 0; i--) {
			for (j = 0; j < i; j++) {
				System.out.print("*");
			}
			for (j = 0; j < 2*(n-i); j++) {
				System.out.print(" ");
			}
			for (j = 0; j < i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}

	}

}
