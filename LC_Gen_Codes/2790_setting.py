class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        n = len(usageLimits)
        groups = [1] * n
        for i in range(1, n):
            if usageLimits[i] > usageLimits[i-1]:
                groups[i] = groups[i-1] + 1
        return max(groups)