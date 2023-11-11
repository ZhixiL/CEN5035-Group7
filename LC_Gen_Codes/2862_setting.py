class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Dictionary to store the count of each number's square root
        freq = {}
        # Iterate through the nums array
        for num in nums:
            # Find the square root of the current number
            sqrt = int(num ** 0.5)
            # Increment the count of the square root in the dictionary
            freq[sqrt] = freq.get(sqrt, 0) + 1
        
        # Initialize the maximum element sum to 0
        max_sum = 0
        
        # Iterate through the dictionary
        for square_root, count in freq.items():
            # If the count is odd, increment the maximum element sum by the square root squared
            if count % 2 != 0:
                max_sum += square_root ** 2
        
        # Return the maximum element sum
        return max_sum