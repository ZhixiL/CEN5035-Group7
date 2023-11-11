class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ops = 0
        
        for i in range(2, n):
            if nums[i-2] < k and nums[i-1] < k and nums[i] < k:
                diff = k - nums[i]
                ops += diff
                nums[i] += diff
        
        return ops