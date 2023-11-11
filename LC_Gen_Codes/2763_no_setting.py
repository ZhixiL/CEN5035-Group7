class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        imbalance_sum = 0
        
        for i in range(n):
            for j in range(i+1, n+1):
                subarray = sorted_nums[i:j]
                imbalance = 0
                
                for k in range(1, len(subarray)):
                    if subarray[k] - subarray[k-1] > 1:
                        imbalance += 1
                
                imbalance_sum += imbalance
        
        return imbalance_sum

# Time complexity: O(n^3)
# Space complexity: O(n)