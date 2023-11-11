class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def isBeautiful(num):
            count_even = 0
            count_odd = 0
            while num > 0:
                digit = num % 10
                if digit % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
                num = num // 10
            return count_even == count_odd
        
        count = 0
        for num in range(low, high+1):
            if num % k == 0 and isBeautiful(num):
                count += 1
                
        return count