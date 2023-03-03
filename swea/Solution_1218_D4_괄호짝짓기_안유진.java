package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Stack;

public class Solution_1218_D4_괄호짝짓기_안유진 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] line;
		Stack<String> stack = new Stack<>();
		HashMap<String, String> hm = new HashMap<>();
		boolean flag = true;
		
		hm.put(")", "(");
		hm.put("}", "{");
		hm.put("]", "[");
		hm.put(">", "<");
		
		for (int test_case = 1; test_case <= 10; test_case++) {
			stack.setSize(0); // 스택 초기화
			flag = true; // flag 초기화
			
			int n = Integer.parseInt(br.readLine());
			line = br.readLine().split("");
			
			for (int i = 0; i < n; i++) {
				if (hm.keySet().contains(line[i])) { // 입력받은 문자열이 닫는 괄호라면
					// stack이 비어있는지 확인해야함!!
					if (!hm.get(line[i]).equals(stack.pop())) { // 스택의 맨 위에 있는 괄호와 비교
						flag = false;
						break;
					}
				} else { // 여는 괄호라면 stack push
					stack.push(line[i]);
				}
			}
			
			// 문자열 입력이 끝난 뒤에도 여는 괄호가 남아있을 경우
			if (stack.size() > 0) flag = false;
			
			if (flag) {
				System.out.printf("#%d 1\n", test_case);
			} else {
				System.out.printf("#%d 0\n", test_case);
			}
		}
	}

}
