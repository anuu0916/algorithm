package kr.co.jungol.beginner;

import java.util.Scanner;

public class JO_1291 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int s = sc.nextInt();
		int e = sc.nextInt();
		
		while (s < 2 || s > 9 || e < 2 || e > 9) {
			System.out.println("INPUT ERROR!");
			s = sc.nextInt();
			e = sc.nextInt();
		}
		
		StringBuilder builder = new StringBuilder();
		if (s < e) {
			for (int j = 1; j < 10; j++) {
				builder.setLength(0);
				for (int i = s; i < e + 1; i++) {
					if (i == s) {
						builder.append(i).append(" * ")
						.append(j).append(" = ")
						.append(i*j);
					} else {
						builder.append("   ").append(i).append(" * ")
						.append(j).append(" = ")
						.append(i*j);
					}
					
				}
				System.out.println(builder.toString());
			}
		} else {
			for (int j = 1; j < 10; j++) {
				builder.setLength(0);
				for (int i = s; i > e - 1; i--) {
					if (i == s) {
						builder.append(i).append(" * ")
						.append(j).append(" = ")
						.append(i*j);
					} else {
						builder.append("   ").append(i).append(" * ")
						.append(j).append(" = ")
						.append(i*j);
					}
					
				}
				System.out.println(builder.toString());
			}
			
		}
	}

}
