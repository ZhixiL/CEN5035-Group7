class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) + 1
        base = [i for i in range(1, n - 1)] + [n, n]
        nums.sort()
        return nums == base

# Test cases
solution = Solution()
print(solution.isGood([2, 1, 3]))  # Output: False
print(solution.isGood([1, 3, 3, 2]))  # Output: True
print(solution.isGood([1, 1]))  # Output: True
print(solution.isGood([3, 4, 4, 1, 2, 1]))  # Output: False