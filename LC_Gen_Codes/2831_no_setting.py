class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        left = 0
        count = {}
        max_len = 0
        max_count = 0
        
        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1
            max_count = max(max_count, count[nums[right]])
            
            if (right - left + 1) - max_count > k:
                count[nums[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len