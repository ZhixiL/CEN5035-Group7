class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        subsequence = []
        prev_group = None
        
        for i in range(n):
            if prev_group is None or groups[i] != prev_group:
                subsequence.append(words[i])
                prev_group = groups[i]
        
        return subsequence