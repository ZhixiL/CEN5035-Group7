Here is the implementation of the `numberOfBeautifulIntegers` function:


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        beautiful_count = 0
        
        for num in range(low, high+1):
            even_count = 0
            odd_count = 0
            
            # Count the number of even and odd digits in the number
            for digit in str(num):
                if int(digit) % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            
            # Check if the number meets both conditions
            if even_count == odd_count and num % k == 0:
                beautiful_count += 1
        
        return beautiful_count


This code defines a class `Solution` and a method `numberOfBeautifulIntegers` which takes in the range `low`, `high`, and `k` as inputs and returns the number of beautiful integers in that range.

The function initializes a variable `beautiful_count` to 0, which will keep track of the count of beautiful integers.

It then iterates over all the numbers in the range `low` to `high` (inclusive) using a for loop. For each number, it counts the number of even and odd digits by iterating over the digits of the number. If the count of even digits is equal to the count of odd digits and the number is divisible by `k`, it increments `beautiful_count` by 1.

Finally, it returns the value of `beautiful_count` as the output.

You can use this code as a reference to solve the given problem.