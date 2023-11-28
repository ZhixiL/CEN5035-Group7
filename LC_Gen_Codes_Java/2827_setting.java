Here is the Java implementation for the given code:

java
class Solution {
    public int numberOfBeautifulIntegers(int low, int high, int k) {
        int count = 0;
        
        for (int num = low; num <= high; num++) {
            if (num % k == 0 && isBeautiful(num)) {
                count++;
            }
        }
        
        return count;
    }
    
    private boolean isBeautiful(int num) {
        int count_even = 0;
        int count_odd = 0;
        
        while (num > 0) {
            int digit = num % 10;
            
            if (digit % 2 == 0) {
                count_even++;
            } else {
                count_odd++;
            }
            
            num = num / 10;
        }
        
        return count_even == count_odd;
    }
}