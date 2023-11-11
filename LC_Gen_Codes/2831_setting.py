class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = 0
        count = {}
        start = max_count = 0
        
        for end in range(n):
            count[nums[end]] = count.get(nums[end], 0) + 1
            max_count = max(max_count, count[nums[end]])
            
            if (end - start + 1 - max_count) > k:
                count[nums[start]] -= 1
                start += 1
                
            max_len = max(max_len, end - start + 1)
            
        return max_len

# The code uses a sliding window approach to find the longest equal subarray.
# The count dictionary is used to keep track of the frequency of each element in the current subarray.
# The max_count variable keeps track of the maximum frequency of any element in the current subarray.
# If the difference between the length of the current subarray and the max_count is greater than k,
# we need to move the left pointer of the window and update the count dictionary and max_count accordingly.
# At each step, we update the max_len variable with the length of the longest equal subarray found so far.
# Finally, we return the max_len as the result.