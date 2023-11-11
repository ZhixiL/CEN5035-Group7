Here's the implementation of the Solution class:


from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            factors = []
            i = 2
            while i * i <= num:
                count = 0
                while num % i == 0:
                    num //= i
                    count += 1
                if count % 2 != 0:
                    factors.append(i)
                i += 1
            if num > 1:
                factors.append(num)
            
            key = tuple(factors)
            if key in freq:
                freq[key] += 1
            else:
                freq[key] = 1
        
        max_sum = float('-inf')
        for key in freq:
            max_sum = max(max_sum, sum(nums[i] for i in range(len(nums)) if self.checkSubset(nums[i], key)))
        
        return max_sum
    
    def checkSubset(self, num, factors):
        for factor in factors:
            if self.isPerfectSquare(num * factor):
                return True
        return False
    
    def isPerfectSquare(self, num):
        root = int(num ** 0.5)
        return root * root == num


You can create an object of the Solution class and call the `maximumSum` method passing the input nums as a parameter. It will return the maximum element-sum of a complete subset of indices.

Note: The `maximumSum` function first calculates the frequency of different factors (excluding the factors with even powers) for each number in the input list. It then checks all possible subsets of the indices and calculates the maximum element-sum for subsets with the same factors. Finally, it returns the maximum element-sum among all subsets.

This implementation uses a nested loop, so the time complexity is O(n^2), where n is the size of the input list.