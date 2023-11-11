class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # check if s1 and s2 are already equal
        if s1 == s2:
            return True
        
        # check if s1 and s2 have the same characters but at different indices
        if sorted(s1) == sorted(s2):
            return True
        
        return False