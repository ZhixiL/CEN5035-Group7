class Solution {
    public boolean isFascinating(int n) {
        // Concatenate n with 2*n and 3*n
        String concat = n + "" + (2 * n) + (3 * n);

        // Count the occurrences of each digit in the concatenated number
        int[] digit_counts = new int[10];
        for (char digit : concat.toCharArray()) {
            digit_counts[Character.getNumericValue(digit)]++;
        }

        // Check if all digits from 1 to 9 occur exactly once and there are no zeros
        for (int i = 1; i < 10; i++) {
            if (digit_counts[i] != 1) {
                return false;
            }
        }
        if (digit_counts[0] != 0) {
            return false;
        }

        return true;
    }
}