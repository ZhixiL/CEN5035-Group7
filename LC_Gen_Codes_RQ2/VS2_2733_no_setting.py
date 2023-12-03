Here's a fast and optimized version of the `findNonMinOrMax` function:


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        min_num = float('inf')
        max_num = float('-inf')
        non_min_or_max = -1
        
        for num in nums:
            if num < min_num:
                non_min_or_max = min_num
                min_num = num
            elif num > max_num:
                non_min_or_max = max_num
                max_num = num
            elif num != min_num and num != max_num:
                non_min_or_max = num
        
        return non_min_or_max


Explanation:

1. We initialize the variables `min_num` and `max_num` to positive and negative infinity, respectively. This ensures that any integer value in the array will be less than `min_num` and greater than `max_num` when we start iterating.

2. We also initialize the variable `non_min_or_max` to -1. This will hold the number that satisfies the condition.

3. We iterate over each number in the array. If the number is less than the current `min_num`, we update both `non_min_or_max` and `min_num`. Similarly, if the number is greater than the current `max_num`, we update both `non_min_or_max` and `max_num`. If the number is neither the current `min_num` nor `max_num`, we update `non_min_or_max` to the number.

4. Finally, we return `non_min_or_max`, which will contain the number that satisfies the condition.

This implementation reduces the number of iterations and comparisons by updating the `min_num`, `max_num`, and `non_min_or_max` variables as we iterate over the array. It also avoids repeatedly calling the `min` and `max` functions, which can be costly for large arrays.