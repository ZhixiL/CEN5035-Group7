class Solution {
    public int sumOfMultiples(int n) {
        // Initialize the sum
        int total = 0;

        // Loop through all numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            // Check if the number is divisible by 3, 5, or 7
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                // Add the number to the sum
                total += i;
            }
        }

        // Return the sum
        return total;
    }
}