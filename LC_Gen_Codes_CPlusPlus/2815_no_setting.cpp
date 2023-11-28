Here is the converted code in Java:

java
import java.util.List;

class Solution {
    public int maxSum(List<Integer> nums) {
        int maxSum = -1;

        // Loop through each pair of numbers
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                // Find the maximum digit in both numbers
                int maxDigit = Integer.MIN_VALUE;
                String num1 = String.valueOf(nums.get(i));
                String num2 = String.valueOf(nums.get(j));

                for (char digit : num1.toCharArray()) {
                    maxDigit = Math.max(maxDigit, digit - '0');
                }
                for (char digit : num2.toCharArray()) {
                    maxDigit = Math.max(maxDigit, digit - '0');
                }

                if (maxDigit == Integer.parseInt(String.valueOf(num1.charAt(0))) || maxDigit == Integer.parseInt(String.valueOf(num2.charAt(0)))) {
                    // Calculate the sum and update maxSum if necessary
                    int pairSum = nums.get(i) + nums.get(j);
                    maxSum = Math.max(maxSum, pairSum);
                }
            }
        }

        return maxSum;
    }
}