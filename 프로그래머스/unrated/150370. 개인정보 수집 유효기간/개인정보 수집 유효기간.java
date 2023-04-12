import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        String[] todayArr = today.split("\\.");
        
        int tyear = Integer.parseInt(todayArr[0]);
        int tmonth = Integer.parseInt(todayArr[1]);
        int tday = Integer.parseInt(todayArr[2]);
        
        Map<String, Integer> termMap = new HashMap<>();
        
        String[] tmp;
        for (int i = 0; i < terms.length; i++){
            tmp = terms[i].split(" ");
            termMap.put(tmp[0], Integer.parseInt(tmp[1]));
        }
        
        int N = privacies.length;
        int[] answer = new int[N];
        int cnt = 0, month;
        int cyear, cmonth, cday;
        for (int i = 0; i < N; i++){
            tmp = privacies[i].split(" ");
            todayArr = tmp[0].split("\\.");
            month = termMap.get(tmp[1]);
            
            cyear = Integer.parseInt(todayArr[0]);
            cmonth = Integer.parseInt(todayArr[1]) - 1;
            cday = Integer.parseInt(todayArr[2]);
            
            cmonth += month;
            if (cmonth > 11) {
                cyear += cmonth / 12;
                cmonth = cmonth % 12;
            }
            
            cmonth++;
            cday --;
            
            if (cday == 0){
                cmonth--;
                cday = 28;
            }
            
            if (cmonth == 0){
                cyear--;
                cmonth = 12;
            }
            
            System.out.printf("%d.%d.%d\n", cyear, cmonth, cday);
            
            if (cyear < tyear || (cyear == tyear && cmonth < tmonth) || (cyear == tyear && cmonth == tmonth && cday < tday)) {
                answer[cnt++] = i + 1;
            }
        }
        
        
        
        
        return Arrays.copyOf(answer, cnt);
    }
}