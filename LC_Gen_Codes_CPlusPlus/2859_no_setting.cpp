class Solution {
    public int sumIndicesWithKSetBits(List<Integer> nums, int k) {
        int sum = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            // Count the number of set bits in the binary representation of indices
            int count = Integer.bitCount(i);
            
            // Check if the count is equal to k
            if (count == k) {
                sum += nums.get(i);
            }
        }
        
        return sum;
    }
}