Here is a fast and optimized version of the given code:

import sys

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_sum = -1
        num_dict = {}
        
        # Create a dictionary to store the maximum digit in each number
        for num in nums:
            max_digit = max(str(num))
            if max_digit in num_dict:
                num_dict[max_digit].append(num)
            else:
                num_dict[max_digit] = [num]
        
        # Loop through each digit pair in the dictionary
        for digit1 in num_dict:
            for digit2 in num_dict:
                if digit1 == digit2:
                    # If the digits are the same, calculate the maximum sum of pairs
                    pair_sum = max(num_dict[digit1]) + min(num_dict[digit1])
                    max_sum = max(max_sum, pair_sum)
                else:
                    # If the digits are different, find the maximum sum of pairs between the two digits
                    pair_sum = max(num_dict[digit1]) + max(num_dict[digit2])
                    max_sum = max(max_sum, pair_sum)
        
        return max_sum

This code avoids unnecessary comparisons by storing the numbers in a dictionary based on their maximum digit. It then calculates the maximum sum of pairs by iterating through the digit pairs in the dictionary and finding the maximum sum between numbers with the same digit and between numbers with different digits.