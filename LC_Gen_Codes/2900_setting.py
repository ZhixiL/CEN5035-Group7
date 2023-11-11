class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        longest_subsequence = []
        for i in range(n):
            subsequence = [i]
            for j in range(i+1, n):
                if groups[subsequence[-1]] != groups[j]:
                    subsequence.append(j)
            if len(subsequence) > len(longest_subsequence):
                longest_subsequence = subsequence
        return [words[i] for i in longest_subsequence]