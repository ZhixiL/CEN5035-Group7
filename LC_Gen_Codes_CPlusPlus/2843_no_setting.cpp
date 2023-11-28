class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int count = 0;
        
        for (int i = low; i <= high; i++) {
            String numStr = Integer.toString(i);
            
            if (numStr.length() % 2 != 0) {
                continue;
            }
            
            int n = numStr.length() / 2;
            
            if (sumOfDigits(numStr, 0, n) == sumOfDigits(numStr, n)) {
                count++;
            }
        }
        
        return count;
    }
    
    private int sumOfDigits(String numStr, int startIndex, int endIndex) {
        int sum = 0;
        
        for (int i = startIndex; i < endIndex; i++) {
            sum += Character.getNumericValue(numStr.charAt(i));
        }
        
        return sum;
    }
}