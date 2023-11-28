import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> getWordsInLongestSubsequence(int n, String[] words, int[] groups) {
        List<String> subsequence = new ArrayList<>();
        Integer prevGroup = null;
        
        for (int i = 0; i < n; i++) {
            if (prevGroup == null || groups[i] != prevGroup) {
                subsequence.add(words[i]);
                prevGroup = groups[i];
            }
        }
        
        return subsequence;
    }
}