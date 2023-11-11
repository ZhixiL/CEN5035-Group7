Here is the implementation of the `minimumSeconds` function:


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = max(nums)
        min_seconds = float('inf')
        
        # Iterate over each possible value to make all elements equal
        for value in range(1, max_value + 1):
            seconds = 0
            
            # Calculate the number of seconds needed to make all elements equal to the current value
            for i in range(n):
                seconds += max(nums[i] - value, 0)
                
            # Update the minimum number of seconds
            min_seconds = min(min_seconds, seconds)
        
        return min_seconds


This implementation calculates the minimum number of seconds needed to make all elements in the array equal by iterating over each possible value between 1 and the maximum value in the array. For each value, it calculates the number of seconds needed by subtracting the current value from each element in the array and summing the positive differences. The function returns the minimum number of seconds among all possible values.