Here is the completed implementation of the `findNonMinOrMax` function in Python:


from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        nums.sort()
        return nums[1]


Explanation:
- The function `findNonMinOrMax` takes an input list `nums` of positive integers.
- It first checks if the length of the list is less than 3. If so, it means there are not enough elements to find a number that is neither the minimum nor the maximum, so it returns -1.
- Otherwise, it sorts the list in ascending order.
- Since the list contains distinct positive integers, the first element after sorting will be the minimum and the last element will be the maximum. Therefore, the number we are looking for is the second element after sorting, which can be accessed using `nums[1]`.
- The function returns this number as the output.