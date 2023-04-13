import java.util.*;

class Solution {
    // 사전순으로 빠른 우선순위 d, l, r, u
    private int[] dr = {1, 0, 0, -1};
    private int[] dc = {0, -1, 1, 0};
    private int N, M, R, C, K;
    private char[] dir;
    private char[] term = {'d', 'l', 'r', 'u'};
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        
        N = n;
        M = m;
        R = r;
        C = c;
        K = k;
        
        dir = new char[k];
        if (dfs(x, y, k, getDiff(x, y))) {
            return String.valueOf(dir);
        } else return "impossible";
        
    }
    
    private boolean dfs(int r, int c, int cnt, int diff){
        if (cnt == 0 && diff == 0) return true;
        
        if (cnt <= 0 || cnt < diff || (cnt%2) != (diff%2)) return false;
        
        int nr, nc;
        for(int i = 0; i < 4; i++){
            nr = r + dr[i];
            nc = c + dc[i];
            
            if (!isValid(nr, nc)) continue;
            
            dir[K-cnt] = term[i];
            if (dfs(nr, nc, cnt-1, getDiff(nr, nc))) return true;
        }
        
        return false;
    }
    
    private boolean isValid(int r, int c){
        if (r < 1|| r > N || c < 1 || c > M) return false;
        return true;
    }
    
    private int getDiff(int r, int c){
        return Math.abs(r-R) + Math.abs(c-C);
    }
}