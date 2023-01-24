package kr.co.jungol.beginner;

import java.util.Scanner;

public class JO_1307 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		char [][] arr = new char [n][n];
		char a = 'A';
		
		for (int i = n-1; i > -1; i--) {
			for (int j = n-1; j > -1; j--) {
				if(a > 'Z') {
					a = 'A';
				}
				arr[j][i] = a++;
			}
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}

	}

}
