class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = [0, 0, 0]
        for num in nums:
            count[num-1] += 1
        
        max_count = max(count)
        return len(nums) - max_count