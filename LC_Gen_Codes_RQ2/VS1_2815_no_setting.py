import typing

class Solution:
    def maxSum(self, nums: typing.List[int]) -> int:
        max_sum = -1
        
        # Loop through each pair of numbers
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Find the maximum digit in both numbers
                max_digit = max(str(nums[i]))
                if max_digit == max(str(nums[j])):
                    # Calculate the sum and update max_sum if necessary
                    pair_sum = nums[i] + nums[j]
                    max_sum = max(max_sum, pair_sum)
        
        return max_sum