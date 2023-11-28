import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> splitWordsBySeparator(List<String> words, char separator) {
        List<String> result = new ArrayList<>();
        for (String word : words) {
            String[] splits = word.split(Character.toString(separator));
            for (String split : splits) {
                if (!split.isEmpty()) {
                    result.add(split);
                }
            }
        }
        return result;
    }
}