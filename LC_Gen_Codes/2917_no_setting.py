class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        nums_len = len(nums)
        result = 0
        
        for i in range(32):  # considering 32 bits in an integer
            count = 0
            
            for num in nums:
                if num & (1 << i) != 0:
                    count += 1
                    
                if count >= k:
                    result |= (1 << i)
                    break
        
        return result