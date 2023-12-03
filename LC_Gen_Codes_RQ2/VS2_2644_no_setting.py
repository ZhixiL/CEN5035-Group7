Here is a more optimized version of the code:

class Solution:
    def maxDivScore(self, nums, divisors):
        max_score = 0
        max_divisor = float('inf')
        
        divisor_counts = dict()  # Store the count of numbers divisible by each divisor
        
        for num in nums:
            for divisor in divisors:
                if num % divisor == 0:
                    if divisor not in divisor_counts:
                        divisor_counts[divisor] = 0
                    divisor_counts[divisor] += 1
                
        for divisor, count in divisor_counts.items():
            if count >= max_score:
                if count > max_score or divisor < max_divisor:
                    max_score = count
                    max_divisor = divisor
        
        return max_divisor

Explanation:
- Instead of calculating the score for each divisor separately, we iterate through each number in `nums` and check if it is divisible by any of the divisors.
- We maintain a `divisor_counts` dictionary to store the count of numbers divisible by each divisor.
- We increment the count for each divisor whenever we encounter a number divisible by that divisor.
- After iterating through all the numbers, we iterate through the `divisor_counts` dictionary to find the divisor with the maximum count.
- We update the `max_score` and `max_divisor` accordingly.
- Finally, we return the `max_divisor`.