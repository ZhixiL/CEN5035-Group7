cpp
class Solution {
public:
    int sumIndicesWithKSetBits(vector<int>& nums, int k) {
        // Initialize the sum variable
        int total_sum = 0;
        
        // Iterate through each number in the nums vector
        for (int i = 0; i < nums.size(); i++) {
            // Convert the index i to its binary representation and count the set bits
            string binary = bitset<32>(i).to_string();
            int num_set_bits = count(binary.begin(), binary.end(), '1');
            
            // If the number of set bits is equal to k, add the corresponding number to the total sum
            if (num_set_bits == k) {
                total_sum += nums[i];
            }
        }
        
        // Return the total sum
        return total_sum;
    }
};