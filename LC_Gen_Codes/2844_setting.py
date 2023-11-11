class Solution:
    def minimumOperations(self, num: str) -> int:
        # Initialize a variable to keep track of the minimum operations
        min_operations = float('inf')
        
        # Iterate through all possible pairs of digits to delete
        for i in range(len(num) - 1):
            for j in range(i+1, len(num)):
                # Create a new string without the selected digits
                new_num = num[:i] + num[i+1:j] + num[j+1:]
                
                # Check if the new number is divisible by 25
                if int(new_num) % 25 == 0:
                    # Update the minimum operations if necessary
                    min_operations = min(min_operations, len(num) - len(new_num))
        
        # Return the minimum operations required
        return min_operations