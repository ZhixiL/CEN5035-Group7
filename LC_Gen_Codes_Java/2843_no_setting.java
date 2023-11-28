Here is the converted code to Java:

java
class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int count = 0;

        for (int i = low; i <= high; i++) {
            String numStr = String.valueOf(i);

            // Numbers with an odd number of digits are never symmetric
            if (numStr.length() % 2 != 0) {
                continue;
            }

            int n = numStr.length() / 2;

            // Check if the sum of the first n digits is equal to the sum of the last n digits
            int sumFirstHalf = 0;
            int sumSecondHalf = 0;
            for (int j = 0; j < n; j++) {
                sumFirstHalf += Integer.parseInt(String.valueOf(numStr.charAt(j)));
                sumSecondHalf += Integer.parseInt(String.valueOf(numStr.charAt(j + n)));
            }
            
            if (sumFirstHalf == sumSecondHalf) {
                count++;
            }
        }

        return count;
    }
}