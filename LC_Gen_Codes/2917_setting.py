class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bitwise_or = 0
        
        for i in range(31):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
            if count >= k:
                bitwise_or += (1 << i)
        
        return bitwise_or