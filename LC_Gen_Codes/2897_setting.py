class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        prefix_sums = [0] * (n+1)
        for i in range(1, n+1):
            prefix_sums[i] = prefix_sums[i-1] + nums[i-1]
        
        max_sum = 0
        for i in range(k, n+1):
            curr_sum = prefix_sums[i] - prefix_sums[i-k]
            max_sum = max(max_sum, curr_sum * curr_sum)
        
        return max_sum % (10**9 + 7)