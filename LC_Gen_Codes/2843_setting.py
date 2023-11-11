class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            if self.isSymmetric(num):
                count += 1
        return count
    
    def isSymmetric(self, num):
        digits = str(num)
        n = len(digits) // 2
        first_half = digits[:n]
        second_half = digits[-n:]
        return sum(map(int, first_half)) == sum(map(int, second_half))