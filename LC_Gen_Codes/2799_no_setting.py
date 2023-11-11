class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            distinct_elements = set()
            for j in range(i, n):
                distinct_elements.add(nums[j])
                if len(distinct_elements) == len(set(nums)):
                    count += 1
                    
        return count