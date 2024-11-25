import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;

class Solution {
    public int removeDuplicates(int[] nums) {

        HashSet<Integer> seen = new HashSet<>();
        List<Integer> n = new ArrayList<>();

        for(int i = 0; i < nums.length; i++){
           if (!seen.contains(nums[i])) {
                seen.add(nums[i]);
                n.add(nums[i]);
            }
        }

        for (int i = 0; i < n.size(); i++) {
            nums[i] = n.get(i);
        }

        return n.size();
    }
}