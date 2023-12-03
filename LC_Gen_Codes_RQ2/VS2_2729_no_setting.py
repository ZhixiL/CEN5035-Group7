Here is an optimized version of the code:


class Solution:
    def isFascinating(self, n: int) -> bool:
        # Concatenate n with 2*n and 3*n
        concat = str(n) + str(2 * n) + str(3 * n)
        
        # Check if all digits from 1 to 9 occur exactly once and there are no zeros
        return len(set(concat)) == len(concat) == 10 and '0' not in concat


Explanation:
1. Instead of counting occurrences of each digit using a list, we can use the `set()` function to get a set of unique digits in `concat`. By comparing the length of the set with the length of `concat` (which should be 10 if all digits from 1-9 occur once and there are no zeros), we can determine if all digits occur exactly once and there are no zeros.
2. We can directly check if '0' is not in `concat` using the `not in` operator.

This code eliminates the need for looping through each digit and counting occurrences, making it faster and more concise.