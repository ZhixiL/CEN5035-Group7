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