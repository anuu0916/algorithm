import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		char[] str = sc.nextLine().toCharArray();
		int[] alphabet = new int[26];
		
		for (char c : str) {
			alphabet[c-'A'] += 1;
		}
		
		int cnt = 0;
		int center = -1;
		for (int i = 0; i < 26; i++) {
			if (alphabet[i] % 2 == 1) {
				cnt++;
				center = i;
			}
			
		}
		
		if (cnt > 1) {
			System.out.println("I'm Sorry Hansoo");
			return;
		}
		
		for (int i = 0; i < 26; i++) {
			if (alphabet[i] > 1) {
				for (int j = 0; j < alphabet[i]/2; j++) {
					sb.append((char)(i+'A'));
				}
			}
		}
		
		System.out.print(sb);
		if (center > -1)
			System.out.print((char)(center + 'A'));
		System.out.println(sb.reverse());
	}

}