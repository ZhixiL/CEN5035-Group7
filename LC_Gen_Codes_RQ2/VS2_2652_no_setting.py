Here's a faster version of the code:

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # Initialize the sum
        total = 0
        
        # Check if n is divisible by 3, 5, or 7
        if n >= 3:
            total += (n // 3) * (3 + n // 3 * 3) // 2
        if n >= 5:
            total += (n // 5) * (5 + n // 5 * 5) // 2
        if n >= 7:
            total += (n // 7) * (7 + n // 7 * 7) // 2
        
        # Return the sum
        return total