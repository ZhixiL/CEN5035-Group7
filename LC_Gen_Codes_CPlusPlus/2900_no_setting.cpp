class Solution {
public:
    vector<string> getWordsInLongestSubsequence(int n, vector<string>& words, vector<int>& groups) {
        vector<string> subsequence;
        int prev_group = -1;
        
        for(int i = 0; i < n; i++){
            if(prev_group == -1 || groups[i] != prev_group){
                subsequence.push_back(words[i]);
                prev_group = groups[i];
            }
        }
        
        return subsequence;
    }
};