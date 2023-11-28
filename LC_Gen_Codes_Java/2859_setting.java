import java.util.List;

class Solution {
    public int sumIndicesWithKSetBits(List<Integer> nums, int k) {
        int total_sum = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            String binary = Integer.toBinaryString(i);
            int num_set_bits = countSetBits(binary);
            
            if (num_set_bits == k) {
                total_sum += nums.get(i);
            }
        }
        
        return total_sum;
    }
    
    private int countSetBits(String binary) {
        int count = 0;
        
        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '1') {
                count++;
            }
        }
        
        return count;
    }
}