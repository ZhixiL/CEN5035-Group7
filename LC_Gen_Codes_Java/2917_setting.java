java
class Solution {
    public int findKOr(int[] nums, int k) {
        int bitwise_or = 0;
        
        for (int i = 0; i < 31; i++) {
            int count = 0;
            for (int num : nums) {
                if (((num >> i) & 1) == 1) {
                    count += 1;
                }
            }
            if (count >= k) {
                bitwise_or += (1 << i);
            }
        }
        
        return bitwise_or;
    }
}