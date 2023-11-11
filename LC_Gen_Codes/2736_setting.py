class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        # Create a list to store the maximum values
        answer = []
        
        # Iterate through each query
        for query in queries:
            xi = query[0]
            yi = query[1]
            
            # Initialize the maximum value to -1
            max_sum = -1
            
            # Iterate through each index j
            for j in range(len(nums1)):
                # Check if nums1[j] >= xi and nums2[j] >= yi
                if nums1[j] >= xi and nums2[j] >= yi:
                    # Update the maximum value if the sum is greater
                    max_sum = max(max_sum, nums1[j] + nums2[j])
            
            # Append the maximum value to the answer list
            answer.append(max_sum)
        
        # Return the answer list
        return answer