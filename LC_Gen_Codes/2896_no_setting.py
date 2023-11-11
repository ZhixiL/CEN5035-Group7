class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        
        # Count the number of differences between s1 and s2
        diff_count = 0
        for i in range(n):
            if s1[i] != s2[i]:
                diff_count += 1
        
        # If the number of differences is odd, it is impossible to make the two strings equal
        if diff_count % 2 != 0:
            return -1
        
        # Calculate the cost of flipping each character from s1 to s2
        cost = 0
        for i in range(n):
            if s1[i] != s2[i]:
                if s1[i] == '0':
                    # If s1[i] is 0 and s2[i] is 1, we can choose the second operation
                    cost += 1
                else:
                    # If s1[i] is 1 and s2[i] is 0, we need to choose the first operation
                    # Check if the cost of flipping two indices is less than flipping a single index
                    if x < 2:
                        cost += x
                    else:
                        cost += 2
        
        return cost