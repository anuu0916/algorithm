package kr.co.jungol.beginner;

import java.util.Scanner;

public class JO_2046 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int [][] arr = new int[n][n];
		
		if (m==1) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					arr[i][j] = i+1;
				}
			}
		} else if (m==2) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (i%2 == 0) {
						arr[i][j] = j+1;
					} else {
						arr[i][j] = n-j;
					}
					
				}
				
			}
		} else if (m==3) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					arr[i][j] = (i+1)*(j+1);
				}
			}
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
		
	}

}
