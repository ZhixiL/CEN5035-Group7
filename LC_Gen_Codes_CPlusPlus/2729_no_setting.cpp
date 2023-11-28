class Solution {
    public boolean isFascinating(int n) {
        // Concatenate n with 2*n and 3*n
        String concat = String.valueOf(n) + String.valueOf(2 * n) + String.valueOf(3 * n);

        // Count the occurrences of each digit in the concatenated number
        int[] digitCounts = new int[10];
        for (char digit : concat.toCharArray()) {
            digitCounts[Character.getNumericValue(digit)]++;
        }

        // Check if all digits from 1 to 9 occur exactly once and there are no zeros
        for (int i = 1; i < 10; i++) {
            if (digitCounts[i] != 1) {
                return false;
            }
        }
        if (digitCounts[0] != 0) {
            return false;
        }

        return true;
    }
}