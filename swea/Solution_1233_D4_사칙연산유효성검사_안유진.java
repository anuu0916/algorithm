package swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Solution_1233_D4_사칙연산유효성검사_안유진 {
	static boolean[] visited;
	static int N;
	static String[] tree;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int test_case = 1; test_case <= 10; test_case++) {
			N = Integer.parseInt(br.readLine());
			visited = new boolean[N + 1];

			String[] tmp;
			tree = new String[N + 1];
			for (int i = 1; i <= N; i++) {
				tmp = br.readLine().split(" ");
				tree[i] = tmp[1];
			}

			System.out.printf("#%d %d\n", test_case, bfs());
		}
	}

	public static int bfs() {
		Queue<Integer> queue = new LinkedList<Integer>();
		int cur;

		queue.offer(1); // root노드의 index를 queue에 저장
		while (!queue.isEmpty()) {
			cur = queue.poll();
			if (cur * 2 <= N && isNumeric(tree[cur]))
				return 0;
			if (cur * 2 > N && !isNumeric(tree[cur]))
				return 0;

			// 왼쪽 노드
			if (cur * 2 <= N)
				queue.offer(cur * 2);
			// 오른쪽 노드
			if (cur * 2 + 1 <= N)
				queue.offer(cur * 2 + 1);

		}

		return 1;

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
