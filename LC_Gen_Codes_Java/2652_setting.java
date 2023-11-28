Here's the equivalent Java code:

java
class Solution {
    public int sumOfMultiples(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                sum += i;
            }
        }
        return sum;
    }
}

// Test the code
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.sumOfMultiples(7));  // Output: 21
        System.out.println(solution.sumOfMultiples(10));  // Output: 40
        System.out.println(solution.sumOfMultiples(9));  // Output: 30
    }
}


Note: If you're running this code outside of an online code editor or an IDE, make sure to name the Java file and class as `Solution`.