class Solution:
    def isFascinating(self, n: int) -> bool:
        # Concatenate n with 2*n and 3*n
        concat = str(n) + str(2 * n) + str(3 * n)
        
        # Count the occurrences of each digit in the concatenated number
        digit_counts = [0] * 10
        for digit in concat:
            digit_counts[int(digit)] += 1
        
        # Check if all digits from 1 to 9 occur exactly once and there are no zeros
        for i in range(1, 10):
            if digit_counts[i] != 1:
                return False
        if digit_counts[0] != 0:
            return False
        
        return True