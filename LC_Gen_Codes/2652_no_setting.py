class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # Initialize the sum
        total = 0
        
        # Loop through all numbers from 1 to n
        for i in range(1, n+1):
            # Check if the number is divisible by 3, 5, or 7
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                # Add the number to the sum
                total += i
        
        # Return the sum
        return total