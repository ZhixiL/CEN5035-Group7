class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # If k is odd, we can start from 1 and add k to each subsequent element
        if k % 2 == 1:
            return n + k * (n - 1) // 2
        
        # If k is even, we need to add an extra element to the array
        # The extra element should be greater than n, but less than the sum of the first n elements
        # The sum of the first n elements can be calculated as n + (n-1) + (n-2) + ... + 1 = n*(n+1)/2
        # To find the minimum possible sum, we can add k+1 to the sum of the first n elements
        return n * (n + 1) // 2 + k // 2 + 1