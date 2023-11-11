Here's the implementation of the `findNonMinOrMax` function:


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        min_num = min(nums)
        max_num = max(nums)
        
        for num in nums:
            if num != min_num and num != max_num:
                return num
        
        return -1


Explanation:

1. We first check if the length of the array `nums` is less than 3. If it is, it means there are not enough elements in the array to find a number that is neither the minimum nor the maximum, so we return -1.

2. Next, we find the minimum value in the array using `min(nums)` and store it in the variable `min_num`. Similarly, we find the maximum value in the array using `max(nums)` and store it in the variable `max_num`.

3. We then iterate over each number in the array. If the number is not equal to either the minimum value or the maximum value, it means it is a number that satisfies the given condition. In that case, we return the number.

4. If we finish the loop without finding a number that satisfies the condition, we return -1.

Note: The `List[int]` type hint in the function declaration indicates that the `nums` parameter should be a list of integers.