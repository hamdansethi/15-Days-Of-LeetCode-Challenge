import java.util.*;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        int n = nums.length;
        
        List<Integer> x =new ArrayList<Integer>();
        
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        
        for(int i = 1; i <= n; i++){
            if(!numSet.contains(i)){
                x.add(i);
            }
        }
        return x;
    }
}