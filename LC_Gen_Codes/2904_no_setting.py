class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        counts = [0] * n
        
        # count the number of 1's in each substring of s
        for i in range(n):
            if s[i] == '1':
                counts[i] = counts[i-1] + 1
            else:
                counts[i] = counts[i-1]
        
        # find the shortest beautiful substring
        min_len = float('inf')
        start, end = -1, -1
        for i in range(n):
            for j in range(i, n):
                count = counts[j] - counts[i-1] if i > 0 else counts[j]
                if count == k and (j-i+1) < min_len:
                    min_len = j - i + 1
                    start, end = i, j
        
        # if no beautiful substring found, return an empty string
        if start == -1 or end == -1:
            return ""
        
        # return the lexicographically smallest beautiful substring
        return s[start:end+1]