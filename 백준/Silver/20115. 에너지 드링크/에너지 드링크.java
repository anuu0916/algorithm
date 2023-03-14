import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk;
		
		int N = Integer.parseInt(br.readLine());
		
		PriorityQueue<Double> queue = new PriorityQueue<>(new Comparator<Double>() {

			@Override
			public int compare(Double o1, Double o2) {
				// TODO Auto-generated method stub
				return Double.compare(o2, o1);
			}
		});
		stk = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			queue.offer(Double.parseDouble(stk.nextToken()));
		}
		
		double a, b;
		while(queue.size() > 1) {
			a = queue.poll();
			b = queue.poll();
			a += b/2;
			queue.offer(a);
		}
		
		System.out.println(queue.poll());
	}

}