package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution_1228_D3_암호문1_안유진 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		List<String> list; 
		
		for (int test_case = 1; test_case <= 10; test_case++) {
			int N = Integer.parseInt(br.readLine());
			list = new LinkedList<String>();
			
			stk = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				list.add(stk.nextToken());
			}
			
			int cmd_num = Integer.parseInt(br.readLine());
			int start, cnt;
			
			stk = new StringTokenizer(br.readLine());
			
			while(stk.hasMoreTokens()) {
				if (stk.nextToken().equals("I")) {
					start = Integer.parseInt(stk.nextToken());
					cnt = Integer.parseInt(stk.nextToken());
					
					for (int i = 0; i < cnt; i++) {
						list.add(start+i, stk.nextToken());
					}

				}
			}
			
			System.out.print("#"+test_case+" ");
			for (int i = 0; i < 10; i++) {
				System.out.print(list.get(i)+" ");
			}
			System.out.println();
			
		}
		
		
		
	}

}
