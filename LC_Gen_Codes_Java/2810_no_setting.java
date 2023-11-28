class Solution {
    public String finalString(String s) {
        StringBuilder result = new StringBuilder();
        StringBuilder stack = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (c == 'i') {
                stack.reverse();
            } else {
                stack.append(c);
            }
        }

        result.append(stack);
        return result.toString();
    }
}