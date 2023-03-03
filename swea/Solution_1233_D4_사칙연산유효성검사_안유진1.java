package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution_1233_D4_사칙연산유효성검사_안유진1 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int test_case = 1; test_case <= 10; test_case++) {
			int N = Integer.parseInt(br.readLine());
			
			int res = 1;
			String[] tmp;
			for (int i = 0; i < N; i++) {
				tmp = br.readLine().split(" ");
				if (tmp.length == 4 && isNumeric(tmp[1])) res = 0;
				else if (tmp.length == 2 && !isNumeric(tmp[1])) res = 0;
			}
			
			System.out.printf("#%d %d\n", test_case, res);
		}

	}
	
	private static boolean isNumeric(String s) {
		try {
			Integer.parseInt(s);
			return true;
		} catch (NumberFormatException e) {
			return false;
		}
	}

}
