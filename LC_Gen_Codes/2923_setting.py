Here is the implementation of the `findChampion` function in Python.


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            is_champion = True
            for j in range(n):
                if i != j and grid[i][j] == 1:
                    is_champion = False
                    break
            if is_champion:
                return i
        return -1


This function iterates through each team `i` and checks if there is any team `j` that is stronger than team `i`. If it finds a team `j` that is stronger than team `i`, it sets the `is_champion` flag to False and breaks the inner loop. If no team `j` is found to be stronger than team `i`, it returns `i` as the champion. If no champion is found, it returns -1.

Please note that this implementation assumes that the input is valid, i.e., it satisfies the given constraints.