class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Initialize the pointers for the subarray
        start, end = 0, 0

        # Initialize the current sum and the minimum length of the subarray
        current_sum = 0
        min_length = float('inf')

        while start < n:
            # Check if the current subarray sum is equal to the target
            if current_sum == target:
                length = end - start
                min_length = min(min_length, length)

            # If the current subarray sum is less than the target, extend the subarray
            if current_sum < target:
                if end < n:
                    current_sum += nums[end]
                    end += 1
                else:
                    break

            # If the current subarray sum is greater than or equal to the target, shrink the subarray
            else:
                current_sum -= nums[start]
                start += 1

        # If there is no subarray with sum equal to the target, return -1
        if min_length == float('inf'):
            return -1

        return min_length