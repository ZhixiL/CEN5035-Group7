class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        # Check if it is possible to make the strings equal
        diff_count = abs(s1.count('1') - s2.count('1'))
        if diff_count % 2 != 0:
            return -1
        
        # Create a list to keep track of the cost of each operation
        costs = []
        
        # Calculate the cost of flipping two adjacent characters
        cost_flip_adjacent = abs(s1.count('1') - s2.count('1')) // 2
        costs.append(cost_flip_adjacent)
        
        # Calculate the cost of flipping two characters with x cost
        cost_flip_x = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cost_flip_x += 1
                if cost_flip_x > x:
                    return -1
        costs.append(cost_flip_x)
        
        # Calculate the cost of flipping two characters with x cost
        cost_flip_x *= x
        
        return min(costs) + cost_flip_x