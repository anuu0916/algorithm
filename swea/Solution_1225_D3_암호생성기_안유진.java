package swea;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Solution_1225_D3_암호생성기_안유진 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Queue<Integer> queue = new LinkedList<Integer>();
		
		for (int test_case = 0; test_case < 10; test_case++) {
			int T = sc.nextInt();
			queue.clear(); // 초기화
			
			// 8개의 데이터 입력
			for (int i = 0; i < 8; i++) {
				queue.offer(sc.nextInt());
			}
			
			int cur = 1; // queue에서 pop한 값을 담을 변수
			while(cur > 0) { // cur가 0보다 클 때 반복 수행
				for (int i = 1; i <= 5; i++) { // 1부터 5까지 감소하는 한 사이클 실행
					cur = queue.poll(); // pop
					cur -= i;
					
					if (cur <= 0) { // 0 이하라면 0을 push하고 break
						queue.offer(0);
						break;
					}
					queue.offer(cur);
				}
			}
			
			// 암호 출력
			System.out.printf("#%d ", T);
			for (int i = 0; i < 8; i++) {
				System.out.print(queue.poll() + " ");
			}
			System.out.println();
		}

	}

}
