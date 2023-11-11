class Solution:
     def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
         score = [0] * len(divisors)  # initialize score array with zeros
         for num in nums:
             for i, divisor in enumerate(divisors):
                 if num % divisor == 0:
                     score[i] += 1  # increment the score if num is divisible by divisor
         max_score = max(score)  # find the maximum score
         max_score_divisors = [divisors[i] for i, s in enumerate(score) if s == max_score]
         return min(max_score_divisors)  # return the minimum of the divisors with maximum score