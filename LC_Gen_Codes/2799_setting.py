Here is the implementation of the countCompleteSubarrays function:


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            distinct_count = {}
            distinct_elements = 0

            for j in range(i, n):
                if nums[j] not in distinct_count:
                    distinct_count[nums[j]] = 1
                    distinct_elements += 1
                else:
                    distinct_count[nums[j]] += 1

                if distinct_elements == len(distinct_count):
                    ans += 1

        return ans


This implementation uses a nested loop to iterate through all possible subarrays. For each subarray, it keeps track of the count of distinct elements using a dictionary named `distinct_count` and a variable named `distinct_elements`.

The outer loop iterates from index `i` to the end of the array. The inner loop iterates from index `j` (starting from `i`) to the end of the array.

In each iteration of the inner loop, it checks if the element at index `j` is already in the `distinct_count` dictionary. If not, it adds it with a count of 1 and increments the `distinct_elements` variable. If it's already in the dictionary, it just increments the count.

After updating the `distinct_count` dictionary and `distinct_elements` variable, it checks if the number of distinct elements in the subarray is equal to the number of distinct elements in the whole array. If it is, it increments the `ans` variable by 1.

Finally, it returns the `ans` variable as the result.