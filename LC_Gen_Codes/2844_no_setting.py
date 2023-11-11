class Solution:
    def minimumOperations(self, num: str) -> int:
        # Initialize the minimum number of operations to infinity
        min_operations = float('inf')
        
        # Iterate through each possible pair of digits to delete
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                # Delete digits at indices i and j
                special_num = num[:i] + num[i+1:j] + num[j+1:]
                
                # If the resulting number is divisible by 25, update the minimum operations
                if int(special_num) % 25 == 0:
                    min_operations = min(min_operations, len(num) - len(special_num))
        
        # If no special number is found, return -1
        if min_operations == float('inf'):
            return -1
        
        return min_operations