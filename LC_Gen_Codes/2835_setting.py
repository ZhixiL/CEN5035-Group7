class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        # Function to calculate the sum of a subsequence
        def subsequenceSum(arr: List[int]) -> int:
            return sum(arr)
        
        # Sort the array in descending order
        nums.sort(reverse=True)
        
        # Initialize the count of operations to 0
        count = 0
        
        # While the target is greater than 0 and nums is not empty
        while target > 0 and nums:
            # If the target is greater than the sum of the current array
            if target > subsequenceSum(nums):
                # Remove the largest element from the array
                largest = nums.pop(0)
                
                # Subtract the largest element from the target
                target -= largest
                
                # Add the two occurrences of largest/2 to the end of the array
                nums.append(largest//2)
                nums.append(largest//2)
                
                # Increment the count of operations
                count += 1
                
            # If the target is equal to the sum of the current array
            elif target == subsequenceSum(nums):
                # Increment the count of operations
                count += 1
                
                # Break out of the loop
                break
            
            # If the target is less than the sum of the current array
            else:
                # Check if removing the largest element from the array will decrease the target
                if target - nums[0] < subsequenceSum(nums) - target:
                    # Remove the largest element from the array
                    largest = nums.pop(0)
                    
                    # Subtract the largest element from the target
                    target -= largest
                    
                    
                # Check if removing the smallest element from the array will decrease the target
                elif target - nums[-1] < subsequenceSum(nums) - target:
                    # Remove the smallest element from the array
                    smallest = nums.pop()
                    
                    # Subtract the smallest element from the target
                    target -= smallest
                    
                
                # If removing either the largest or smallest element does not decrease the target
                else:
                    # Remove both the largest and smallest elements from the array
                    largest = nums.pop(0)
                    smallest = nums.pop()
                    
                    # Subtract both elements from the target
                    target -= largest + smallest
                    
                # Increment the count of operations
                count += 1
        
        # If the target is greater than 0 or nums is empty, return -1
        if target > 0 or not nums:
            return -1
        
        # Otherwise, return the count of operations
        return count