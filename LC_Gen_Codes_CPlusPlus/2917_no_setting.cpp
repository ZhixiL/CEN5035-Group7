cpp
class Solution {
public:
    int findKOr(vector<int>& nums, int k) {
        int nums_len = nums.size();
        int result = 0;
        
        for (int i = 0; i < 32; i++) {  // considering 32 bits in an integer
            int count = 0;
            
            for (int num : nums) {
                if ((num & (1 << i)) != 0) {
                    count += 1;
                }
                
                if (count >= k) {
                    result |= (1 << i);
                    break;
                }
            }
        }
        
        return result;
    }
};