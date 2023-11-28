Here's the converted Java code:

java
import java.util.List;

class Solution {
    public boolean isAcronym(List<String> words, String s) {
        String acronym = "";
        for (String word : words) {
            acronym += word.charAt(0);
        }
        return acronym.equals(s);
    }
}