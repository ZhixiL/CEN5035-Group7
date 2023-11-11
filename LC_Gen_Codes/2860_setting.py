Here is the implementation of the countWays function:


class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        selected = [0] * n
        unselected = [0] * n
        
        for i in range(n):
            selected[i] = max(nums[i], n - nums[i])
            unselected[i] = n - selected[i]
        
        return len(set(selected)) + len(set(unselected))


In this implementation, we iterate through the given array `nums` and calculate two arrays: `selected` and `unselected`. The `selected` array stores the maximum number of students that need to be selected for each student to be happy, and the `unselected` array stores the maximum number of students that need to be unselected for each student to be happy.

We then return the sum of the lengths of the unique values in the `selected` and `unselected` arrays, as this represents the number of different ways to select a group of students such that everyone remains happy.