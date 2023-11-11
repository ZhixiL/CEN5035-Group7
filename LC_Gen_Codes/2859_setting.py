class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # Initialize the sum variable
        total_sum = 0
        
        # Iterate through each number in the nums array
        for i in range(len(nums)):
            # Convert the index i to its binary representation and count the set bits
            binary = bin(i)[2:]  # [2:] is used to remove the '0b' prefix from the binary representation
            num_set_bits = binary.count('1')
            
            # If the number of set bits is equal to k, add the corresponding number to the total sum
            if num_set_bits == k:
                total_sum += nums[i]
        
        # Return the total sum
        return total_sum