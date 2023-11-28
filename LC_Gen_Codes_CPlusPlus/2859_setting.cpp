cpp
class Solution {
public:
    int sumIndicesWithKSetBits(vector<int>& nums, int k) {
        int total_sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            // Convert the index i to its binary representation and count the set bits
            string binary = bitset<32>(i).to_string();
            int num_set_bits = count(binary.begin(), binary.end(), '1');
            
            // If the number of set bits is equal to k, add the corresponding number to the total sum
            if (num_set_bits == k) {
                total_sum += nums[i];
            }
        }
        
        return total_sum;
    }
};