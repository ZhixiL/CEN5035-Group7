class Solution {
    public List<String> splitWordsBySeparator(List<String> words, char separator) {
        List<String> result = new ArrayList<>();
        for (String word : words) {
            String[] splits = word.split(Character.toString(separator));
            for (String split : splits) {
                if (!split.equals("")) {
                    result.add(split);
                }
            }
        }
        return result;
    }
}