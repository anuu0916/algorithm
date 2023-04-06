import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, K, cnt, step;
	static int[][] belt;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(stk.nextToken());
		K = Integer.parseInt(stk.nextToken());
		
		belt = new int[2*N][2];
		
		stk = new StringTokenizer(br.readLine());
		for (int i = 0; i < 2*N; i++) {
			belt[i][0] = Integer.parseInt(stk.nextToken());
		}
		
		
		int up = 0;
		int down = N-1;
		cnt = 0;
		step = 0;
		while(cnt < K) {
			step++;
			
			// 한 칸 회전
			if (--up < 0) {
				up = 2*N-1;
			}
			
			if (--down < 0) {
				down = 2*N-1;
			}
			
			// 로봇 이동
			moveRobots(down);
			
			// 로봇 올리기
			if (belt[up][0] > 0) {
				belt[up][1] = 1;
				if (--belt[up][0] == 0) cnt++;
			}
			
		}
		
		System.out.println(step);
	}
	
	private static void moveRobots(int down) {
		// 내리는 위치 로봇 내리기
		belt[down][1] = 0;
		
		int cur = down, next;
		
		// 로봇 이동
		for (int i = 1; i < N; i++) {
			if (--cur < 0) {
				cur = 2*N-1;
			}
			next = (cur+1) % (2*N);
			// 지금 위치에 로봇이 올라가 있고, 다음 위치의 내구도가 0 이상이면서 올라가있는 로봇이 없을 때
			if (belt[cur][1] == 1 && belt[next][0] > 0 && belt[next][1] == 0) {
				belt[cur][1] = 0;
				belt[next][1] = 1;
				if (--belt[next][0] == 0) cnt++;
				
				// 로봇이 내리는 위치로 이동했다면 즉시 내림
				if (next == down) {
					belt[next][1] = 0;
				}
			}
			
			
		}
	}

}