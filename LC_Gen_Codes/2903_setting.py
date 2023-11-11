class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]

# Explanation:
# We can iterate through all possible pairs of indices (i, j) where i < j and check if the conditions are satisfied.
# If we find a pair that satisfies the conditions, we return that pair as the answer.
# If we don't find any such pair, we return [-1, -1] as the answer.