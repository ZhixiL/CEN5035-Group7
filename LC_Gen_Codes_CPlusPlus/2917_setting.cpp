Here's the provided Python code converted to C++:

cpp
class Solution {
public:
    int findKOr(vector<int>& nums, int k) {
        int bitwise_or = 0;
        
        for (int i = 0; i < 31; i++) {
            int count = 0;
            for (int num : nums) {
                if ((num >> i) & 1) {
                    count++;
                }
            }
            if (count >= k) {
                bitwise_or += (1 << i);
            }
        }
        
        return bitwise_or;
    }
};