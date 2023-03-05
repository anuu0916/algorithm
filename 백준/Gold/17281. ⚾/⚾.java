import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] hitters; // 선수들의 이닝별 결과
	static int[] order; // 타순
	static int maxScore; // 최대 점수

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		hitters = new int[N][9];

		StringTokenizer stk;
		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			for (int j = 0; j < 9; j++) {
				hitters[i][j] = Integer.parseInt(stk.nextToken());
			}
		}

		// 1번 선수(코드에서는 0번)를 제외하고 순열 구하기
		order = new int[8];
		for (int i = 0; i < 8; i++) {
			order[i] = i + 1;
		}

		do {
			simulate();
		} while (np());
		
		System.out.println(maxScore);
	}

	private static void simulate() {
		Queue<Integer> queue = new ArrayDeque<>();
		
		for (int i = 0; i < 9; i++) {
			// 4번타자는 1번선수
			if (i == 3) {
				queue.offer(0);
				continue;
			}
			
			if (i > 3) {
				queue.offer(order[i-1]);
			} else queue.offer(order[i]);
		}

		// 이닝별 득점
		int score = 0;
		int cur, hit; // 현재 타자 번호, 공을 치고 난 결과
		int out = 0;
		int[] field; // 루
		for (int i = 0; i < N; i++) {
			out = 0;
			field = new int[4];
			
			// 1: 안타, 2: 2루타, 3: 3루타, 4: 홈런, 4: 아웃
			while (true) {
				cur = queue.poll();
				hit = hitters[i][cur];
				if (hit == 0) {
					out++;
				} else {
					boolean flag = true;
					for (int j = 0; j < 4; j++) {
						if (flag && field[j] == 0) {
							field[j] = hit;
							flag = false;
						}
						else if (field[j] > 0) field[j] += hit;
						
						if (field[j] > 3) {
							score++;
							field[j] = 0;
						}
					}
				}
				
				queue.offer(cur);
				
				if (out == 3) break;
			}
		}
		
		maxScore = Math.max(maxScore, score);

	}

	private static boolean np() {
		int n = 8;

		int i = n - 1;
		while (i > 0 && order[i - 1] >= order[i])
			i--;

		if (i == 0)
			return false;

		int j = n - 1;
		while (order[i - 1] >= order[j])
			j--;

		swap(i - 1, j);

		int k = n - 1;
		while (i < k) {
			swap(i++, k--);
		}

		return true;
	}

	private static void swap(int i, int j) {
		int tmp = order[i];
		order[i] = order[j];
		order[j] = tmp;
	}

}