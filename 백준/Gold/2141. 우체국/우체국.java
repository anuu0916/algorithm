import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		StringTokenizer stk;
		int x, a;
		long sum = 0;

		int[][] village = new int[N][2];

		for (int i = 0; i < N; i++) {
			stk = new StringTokenizer(br.readLine());
			x = Integer.parseInt(stk.nextToken());
			a = Integer.parseInt(stk.nextToken());

			village[i][0] = x;
			village[i][1] = a;
			sum += a;
		}

		Arrays.sort(village, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				if (o1[0] == o2[0]) {
					return Integer.compare(o1[1], o2[1]);
				} else {
					return Integer.compare(o1[0], o2[0]);
				}
			}
		});

		long people = 0;
		long half = (sum+1)/2;

		for (int i = 0; i < N; i++) {
			people += village[i][1];

			if (people >= half) {
				System.out.println(village[i][0]);
				break;
			}
		}

	}

}