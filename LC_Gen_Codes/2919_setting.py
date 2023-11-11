class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        n = len(nums)
        
        if n < 3:
            return 0
        
        for i in range(2, n):
            if nums[i] < k:
                operations += k - nums[i]
                nums[i] = k
        
        return operations