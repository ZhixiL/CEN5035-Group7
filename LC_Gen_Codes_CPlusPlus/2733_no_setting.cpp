java
import java.util.List;

class Solution {
    public int findNonMinOrMax(List<Integer> nums) {
        if (nums.size() < 3) {
            return -1;
        }
        
        int min_num = Integer.MAX_VALUE;
        int max_num = Integer.MIN_VALUE;
        
        for (int num : nums) {
            min_num = Math.min(min_num, num);
            max_num = Math.max(max_num, num);
        }
        
        for (int num : nums) {
            if (num != min_num && num != max_num) {
                return num;
            }
        }
        
        return -1;
    }
}