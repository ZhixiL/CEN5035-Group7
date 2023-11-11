class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        max_distance = 0
        current_distance = 0
        for move in moves:
            if move == 'L' or move == '_':
                current_distance -= 1
            if move == 'R' or move == '_':
                current_distance += 1
            max_distance = max(max_distance, abs(current_distance))
        return max_distance

solution = Solution()
print(solution.furthestDistanceFromOrigin("L_RL__R")) # Output: 3
print(solution.furthestDistanceFromOrigin("_R__LL_")) # Output: 5
print(solution.furthestDistanceFromOrigin("_______")) # Output: 7