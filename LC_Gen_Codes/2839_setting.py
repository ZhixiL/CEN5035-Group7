class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        
        for char in s1:
            count1[ord(char) - ord('a')] += 1
        
        for char in s2:
            count2[ord(char) - ord('a')] += 1
        
        if count1 == count2:
            return True
        else:
            return False