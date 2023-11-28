java
import java.util.List;

class Solution {
    public int findKOr(List<Integer> nums, int k) {
        int numsLen = nums.size();
        int result = 0;
        
        for (int i = 0; i < 32; i++) { // considering 32 bits in an integer
            int count = 0;
            
            for (int num : nums) {
                if ((num & (1 << i)) != 0) {
                    count++;
                }
                
                if (count >= k) {
                    result |= (1 << i);
                    break;
                }
            }
        }
        
        return result;
    }
}