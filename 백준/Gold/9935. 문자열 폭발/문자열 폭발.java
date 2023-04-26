import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	static int bomblen;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		String bomb = br.readLine();
		bomblen = bomb.length();
		
		Stack<Character> stack = new Stack<>();
		
		for (int i = 0; i < str.length(); i++) {
			stack.add(str.charAt(i));
			
			if (stack.size() >= bomblen) {
				if (check(stack, bomb)) {
					for (int j = 0; j < bomblen; j++) {
						stack.pop();
					}
				}
			}
		}
		
		if (stack.size() == 0) System.out.println("FRULA");
		else {
			StringBuilder sb = new StringBuilder();
			for (char c : stack) {
				sb.append(c);
			}
			System.out.println(sb.toString());
		}
		
	}

	private static boolean check(Stack<Character> stack, String bomb) {
		for (int i = 0; i < bomblen; i++) {
			if (stack.get(stack.size() - bomblen + i) != bomb.charAt(i)) return false; 
		}
		return true;
	}

}