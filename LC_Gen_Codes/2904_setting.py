Here is the implementation of the function shortestBeautifulSubstring:


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        count = [0] * 26
        start = 0
        min_len = float('inf')
        min_start = -1

        for i in range(n):
            count[ord(s[i]) - ord('a')] += 1
            if count[ord(s[i]) - ord('a')] == k:
                unique_count = len(set(s[start:i+1]))
                if unique_count == k:
                    while count[ord(s[start]) - ord('a')] > k:
                        count[ord(s[start]) - ord('a')] -= 1
                        start += 1
                    if i - start + 1 < min_len:
                        min_len = i - start + 1
                        min_start = start
        if min_start != -1:
            return s[min_start:min_start+min_len]
        else:
            return ""


The function maintains a sliding window approach to find beautiful substrings. It counts the frequencies of each character using an array and calculates the number of unique characters in the window. If the unique count is equal to k and the length of the window is smaller than the current minimum length, the start and length of the window are updated.

At the end, if a beautiful substring is found (min_start != -1), it returns the substring with the minimum length. Otherwise, it returns an empty string.