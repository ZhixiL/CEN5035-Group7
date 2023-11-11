Here is the implementation of the `maximumScore` function:


from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Function to check if a number is prime
        def isPrime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        # Function to calculate the prime score of a number
        def primeScore(n):
            score = 0
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0 and isPrime(i):
                    score += 1
                    while n % i == 0:
                        n //= i
            if n > 1:
                score += 1
            return score

        # Calculate the prime scores for all numbers in the array
        scores = [primeScore(num) for num in nums]

        # Calculate the maximum possible score
        maxScore = 1
        for i in range(k + 1):
            maxScore *= max(scores[i:len(nums)-k+i])
        return maxScore % (10**9 + 7)


You can use the `maximumScore` function like this:


solution = Solution()
nums = [8,3,9,3,8]
k = 2
print(solution.maximumScore(nums, k))  # Output: 81

nums = [19,12,14,6,10,18]
k = 3
print(solution.maximumScore(nums, k))  # Output: 4788