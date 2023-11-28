import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> getWordsInLongestSubsequence(int n, List<String> words, List<Integer> groups) {
        List<String> subsequence = new ArrayList<>();
        Integer prev_group = null;
        
        for (int i = 0; i < n; i++) {
            if (prev_group == null || !groups.get(i).equals(prev_group)) {
                subsequence.add(words.get(i));
                prev_group = groups.get(i);
            }
        }
        
        return subsequence;
    }
}