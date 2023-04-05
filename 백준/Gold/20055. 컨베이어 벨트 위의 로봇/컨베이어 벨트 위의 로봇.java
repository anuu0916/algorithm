import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int N, K, cnt, step;
	static List<int[]> belt = new LinkedList<>();
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(stk.nextToken());
		K = Integer.parseInt(stk.nextToken());
		
		stk = new StringTokenizer(br.readLine());
		for (int i = 0; i < 2*N; i++) {
			belt.add(new int[] {Integer.parseInt(stk.nextToken()), 0});
		}
		
		cnt = 0;
		step = 0;
		while(cnt < K) {
			step++;
			// 내리는 위치의 로봇 내리기
			belt.get(N-1)[1] = 0;
			
			// 한 칸 회전
			belt.add(0, belt.remove(2*N-1));
			
			// 로봇 이동
			moveRobots();
			
			// 로봇 올리기
			if (belt.get(0)[0] > 0) {
				belt.get(0)[1] = 1;
				if (--belt.get(0)[0] == 0) cnt++;
			}
			
		}
		
		System.out.println(step);
	}
	
	private static void moveRobots() {
		// 내리는 위치 로봇 내리기
		belt.get(N-1)[1] = 0;
		
		// 로봇 이동
		for (int i = N-2; i > -1; i--) {
			// 지금 위치에 로봇이 올라가 있고, 다음 위치의 내구도가 0 이상이면서 올라가있는 로봇이 없을 때
			if (belt.get(i)[1] == 1 && belt.get(i+1)[0] > 0 && belt.get(i+1)[1] == 0) {
				belt.get(i)[1] = 0;
				belt.get(i+1)[1] = 1;
				if (--belt.get(i+1)[0] == 0) cnt++;
				
				// 로봇이 내리는 위치로 이동했다면 즉시 내림
				if (i+1 == N-1) {
					belt.get(i+1)[1] = 0;
				}
			}
		}
	}

}