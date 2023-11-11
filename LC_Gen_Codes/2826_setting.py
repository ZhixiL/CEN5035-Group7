class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count_changes = 0
        
        group1 = [i for i, num in enumerate(nums) if num == 1]
        group2 = [i for i, num in enumerate(nums) if num == 2]
        group3 = [i for i, num in enumerate(nums) if num == 3]
        
        count_changes += len(group1) - len(nums) // 3  # number of changes needed in group 1
        count_changes += len(group2) - len(nums) // 3  # number of changes needed in group 2
        count_changes += len(group3) - len(nums) // 3  # number of changes needed in group 3
        
        return count_changes