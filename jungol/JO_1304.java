package kr.co.jungol.beginner;

import java.util.Scanner;

public class JO_1304 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		for (int i = 1; i < n+1; i++) {
			for (int j = 0; j < n; j++) {
				System.out.print(i+(n*j)+" ");
			}
			System.out.println();
		}
	}

}
