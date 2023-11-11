class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums) # get the maximum element in the array
        base = [i for i in range(1,n)] + [n,n] # create the base array
        
        nums.sort() # sort the nums array
        
        return nums == base # check if nums is equal to base array