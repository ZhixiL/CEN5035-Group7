class Solution:
    def isFascinating(self, n: int) -> bool:
        # Concatenate n, 2*n, and 3*n
        num_str = str(n) + str(2*n) + str(3*n)
        
        # Check if the concatenated string contains all the digits from 1 to 9 exactly once
        # and does not contain any 0's
        digits = set(num_str)
        return len(digits) == 9 and '0' not in digits