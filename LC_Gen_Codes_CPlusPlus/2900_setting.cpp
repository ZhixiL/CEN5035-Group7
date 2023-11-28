cpp
class Solution {
public:
    vector<string> getWordsInLongestSubsequence(int n, vector<string>& words, vector<int>& groups) {
        vector<string> longest_subsequence;
        for (int i = 0; i < n; i++) {
            vector<int> subsequence;
            subsequence.push_back(i);
            for (int j = i+1; j < n; j++) {
                if (groups[subsequence.back()] != groups[j]) {
                    subsequence.push_back(j);
                }
            }
            if (subsequence.size() > longest_subsequence.size()) {
                longest_subsequence.clear();
                for (int k : subsequence) {
                    longest_subsequence.push_back(words[k]);
                }
            }
        }
        return longest_subsequence;
    }
};