Here's the implementation of the `findNonMinOrMax` function in C++:

cpp
class Solution {
public:
    int findNonMinOrMax(vector<int>& nums) {
        if (nums.size() < 3) {
            return -1;
        }
        
        int min_num = *min_element(nums.begin(), nums.end());
        int max_num = *max_element(nums.begin(), nums.end());
        
        for (int num : nums) {
            if (num != min_num && num != max_num) {
                return num;
            }
        }
        
        return -1;
    }
};