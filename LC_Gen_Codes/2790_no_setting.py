class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        n = len(usageLimits)
        groups = [[]]

        for i in range(n):
            count = 0
            for j in range(i+1):
                count += len(groups[j])

            if count <= usageLimits[i]:
                groups.append([k for k in range(i+1)])
            else:
                groups[-1].append(i)

        return len(groups)