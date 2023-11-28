import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> getWordsInLongestSubsequence(int n, String[] words, int[] groups) {
        List<String> longestSubsequence = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            List<Integer> subsequence = new ArrayList<>();
            subsequence.add(i);
            for (int j = i + 1; j < n; j++) {
                if (groups[subsequence.get(subsequence.size() - 1)] != groups[j]) {
                    subsequence.add(j);
                }
            }
            if (subsequence.size() > longestSubsequence.size()) {
                longestSubsequence = subsequence;
            }
        }
        List<String> result = new ArrayList<>();
        for (int index : longestSubsequence) {
            result.add(words[index]);
        }
        return result;
    }
}