import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static int N, M;
	static String expr;
	static int max = Integer.MIN_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		expr = br.readLine();

		subset(0, 0);

		System.out.println(max);

	}

	private static void subset(int cnt, int sum) {
		if (cnt > N - 1) {
			max = Math.max(max, sum);
			return;
		}

		char op = cnt == 0 ? '+' : expr.charAt(cnt - 1);

		// 선택하는 경우
		if (cnt < N-1) {
			int bracket = calculate(expr.charAt(cnt) - '0', expr.charAt(cnt + 2) - '0', expr.charAt(cnt + 1));
			subset(cnt + 4, calculate(sum, bracket, op));
		}

		// 선택하지 않는 경우
		subset(cnt + 2, calculate(sum, expr.charAt(cnt) - '0', op));

	}

	private static int calculate(int a, int b, int opr) {
		int sum = a;

		switch (opr) {
		case '+':
			sum += b;
			break;
		case '-':
			sum -= b;
			break;
		case '*':
			sum *= b;
		}

		return sum;
	}

}