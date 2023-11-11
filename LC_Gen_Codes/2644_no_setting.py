Here is the implementation of the maxDivScore function:


class Solution:
    def maxDivScore(self, nums, divisors):
        max_score = 0
        max_divisor = float('inf')
        
        for divisor in divisors:
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1
            
            if score >= max_score:
                if score > max_score or divisor < max_divisor:
                    max_score = score
                    max_divisor = divisor
        
        return max_divisor


Explanation:
- Initialize `max_score` to 0 and `max_divisor` to infinity.
- Iterate through each `divisor` in the `divisors` list.
- For each `divisor`, initialize a `score` variable to 0.
- Iterate through each `num` in the `nums` list.
- If the `num` is divisible by the current `divisor` (i.e., `num % divisor == 0`), increment the `score` by 1.
- After calculating the `score` for the current `divisor`, check if it is greater than or equal to the `max_score`.
- If the `score` is strictly greater than the `max_score` or it is equal to the `max_score` but the current `divisor` is smaller than the `max_divisor`, update the `max_score` and `max_divisor` accordingly.
- Finally, return the `max_divisor`.