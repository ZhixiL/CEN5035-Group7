Here is the complete implementation of the given function in C++:

cpp
class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        int n = nums.size();
        int special_sum = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                special_sum += nums[i-1] * nums[i-1];
            }
        }
        return special_sum;
    }
};