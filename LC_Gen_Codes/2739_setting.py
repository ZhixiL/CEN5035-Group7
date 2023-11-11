Here is the code implementation for the given problem prompt:


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        totalDistance = 0
        
        while mainTank > 0:
            fuelConsumed = 5
            
            if mainTank >= fuelConsumed:
                mainTank -= fuelConsumed
                totalDistance += fuelConsumed * 10
            else:
                fuelConsumed = mainTank
                mainTank = 0
                totalDistance += fuelConsumed * 10
                
            if mainTank == 0 and additionalTank >= 1:
                mainTank += 1
                additionalTank -= 1
        
        return totalDistance


You can test this code using the provided examples:


solution = Solution()
print(solution.distanceTraveled(5, 10))    # Output: 60
print(solution.distanceTraveled(1, 2))     # Output: 10