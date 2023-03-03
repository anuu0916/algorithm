package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution_1208_D3_Flatten_안유진 {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int dump_num;
		int[] boxes = new int[100];
		String[] tmp;
		
		for (int test_case = 1; test_case < 11; test_case++) {
			dump_num = Integer.parseInt(br.readLine());
			tmp = br.readLine().split(" ");
			
			for (int i = 0; i < 100; i++) {
				boxes[i] = Integer.parseInt(tmp[i]);
			}
			
			for (int i = 0; i < dump_num; i++) {
				Arrays.sort(boxes);
				if (boxes[99] - boxes[0] < 2) {
					break;
				}
				boxes[0] += 1;
				boxes[99] -= 1;
			}
			Arrays.sort(boxes);
			System.out.printf("#%d %d\n", test_case, boxes[99]-boxes[0]);
		}
		
	}

}
