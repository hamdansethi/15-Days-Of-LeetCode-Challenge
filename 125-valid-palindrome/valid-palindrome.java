import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean isPalindrome(String s) {
        
        String lower = s.toLowerCase();

        char[] c = lower.toCharArray();

        List<Character> n = new ArrayList<>();

        for(int i = 0; i < c.length; i++){
            if(Character.isLetterOrDigit(c[i])){
                n.add(c[i]);
            }
        }

        for(int i = 0; i < n.size()/2; i++){
            if(n.get(i) != n.get(n.size() - 1 - i)){
                return false;
            }
        }
        return true;
    }
}