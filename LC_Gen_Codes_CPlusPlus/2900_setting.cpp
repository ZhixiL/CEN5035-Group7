class Solution {
public:
    vector<string> getWordsInLongestSubsequence(int n, vector<string>& words, vector<int>& groups) {
        vector<int> longest_subsequence;
        for (int i = 0; i < n; i++) {
            vector<int> subsequence;
            subsequence.push_back(i);
            for (int j = i+1; j < n; j++) {
                if (groups[subsequence.back()] != groups[j]) {
                    subsequence.push_back(j);
                }
            }
            if (subsequence.size() > longest_subsequence.size()) {
                longest_subsequence = subsequence;
            }
        }
        vector<string> result;
        for (int i : longest_subsequence) {
            result.push_back(words[i]);
        }
        return result;
    }
};