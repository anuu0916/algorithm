import java.util.*;
import java.io.*;

class Solution {
    private int[][] prices, users;
    private int U, E;
    private int[] discount;
    private int maxPlus = -1, maxPrice = -1;
    
    public int[] solution(int[][] users, int[] emoticons) {
        U = users.length;
        E = emoticons.length;
        prices = new int[E][5];
        discount = new int[E];
        this.users = users;
        
        for(int i=0; i < E; i++){
            for(int j=0; j < 5; j++){
                prices[i][j] = emoticons[i] * (100 - (j * 10)) / 100;
            }
        }
        
        permutation(0);
        
        int[] answer = {maxPlus, maxPrice};
        return answer;
    }
    
    private void permutation(int cnt){
        if (cnt == E){
            calc();
            return;
        }
        
        for(int i=1; i < 5; i++){
            discount[cnt] = i;
            permutation(cnt+1);
        }
    }
    
    private void calc() {

        int plus = 0, price = 0;
        int user = 0;
        for(int i = 0; i < U; i++){
            user = 0;
            for(int j = 0; j < E; j++){
                if (users[i][0] <= (discount[j] * 10)){
                    user += prices[j][discount[j]];
                }
                
                if (user >= users[i][1]){
                    plus++;
                    user = 0;
                    break;
                }
                
            }
            price += user;
        }
        
        if (maxPlus < plus){
            maxPlus = plus;
            maxPrice = price;
        } else if (maxPlus == plus) {
            maxPrice = Math.max(maxPrice, price);
        }
    }
}