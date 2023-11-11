class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n):
            selected = 0
            not_selected = 0
            
            for j in range(n):
                if i != j:
                    if nums[j] > nums[i]:
                        selected += 1
                    elif nums[j] < nums[i]:
                        not_selected += 1
            
            if selected > not_selected:
                count += 1
        
        return count