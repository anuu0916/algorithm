import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		char[] text = br.readLine().toCharArray();
		char[] pattern = br.readLine().toCharArray();

		long pHash = 0, tHash = 0, power = 1;
		long base = 5381;
		long mod = 1000000009; // 충돌이 발생하지 않게 최대한 큰 값
		int tlen = text.length;
		int plen = pattern.length;
		
		if (plen > tlen) {
			System.out.println(0);
			System.exit(0);
		}

		// pattern이 일치하는 시작 인덱스
		Deque<Integer> list = new ArrayDeque<>();

		// pattern의 개수만큼 본문의 hash와 pattern의 hash를 구하기
		for (int i = 0; i < plen; i++) {
			pHash = (pHash * base) % mod;
			pHash = (pHash + pattern[i]) % mod;
			tHash = (tHash * base) % mod;
			tHash = (tHash + text[i]) % mod;

			if (i < plen - 1)
				power = (power * base) % mod;
		}

		if (pHash == tHash) {
			list.add(1);
		}

		for (int i = 1; i <= tlen - plen; i++) {
			// 본문의 새로운 hash 만들기
			// 윈도우의 맨 앞부분을 빼주고 윈도우의 맨 뒷부분 추가
			tHash = (((tHash - (text[i - 1] * power) % mod + mod) % mod * base) + text[i + plen - 1]) % mod;

			if (pHash == tHash) {
				list.add(i + 1);
			}
		}

		System.out.println(list.size());
		for (int index : list) {
			System.out.print(index + " ");
		}

	}

}