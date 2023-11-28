Here is the converted code snippet in C++:

cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxSum(std::vector<int>& nums) {
        int max_sum = -1;
        
        // Loop through each pair of numbers
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                // Find the maximum digit in both numbers
                int max_digit = *std::max_element(std::begin(std::to_string(nums[i])), std::end(std::to_string(nums[i])));
                if (max_digit == *std::max_element(std::begin(std::to_string(nums[j])), std::end(std::to_string(nums[j])))) {
                    // Calculate the sum and update max_sum if necessary
                    int pair_sum = nums[i] + nums[j];
                    max_sum = std::max(max_sum, pair_sum);
                }
            }
        }
        
        return max_sum;
    }
};


Note: C++ doesn't have a built-in max function to find the maximum digit in a number. Therefore, we need to convert each number to a string and then find the maximum element using the std::max_element from the algorithm library.