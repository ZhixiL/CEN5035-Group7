class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        def dfs(nums, index, target, memo):
            if target == 0:
                return 0
            if index == len(nums) or target < 0:
                return float('inf')
            if (index, target) in memo:
                return memo[(index, target)]
            
            operations = float('inf')
            if nums[index] <= target:
                operations = min(operations, 1 + dfs(nums, index+1, target - nums[index], memo))
            
            operations = min(operations, dfs(nums, index+1, target, memo))
            
            memo[(index, target)] = operations
            return operations
        
        memo = {}
        operations = dfs(nums, 0, target, memo)
        return -1 if operations == float('inf') else operations