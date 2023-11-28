class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int distance = mainTank * 10; // Calculate the initial distance traveled based on fuel in main tank
        int remainingFuel = mainTank; // Keep track of remaining fuel in main tank
        
        while (remainingFuel >= 5) { // As long as there is at least 5 liters of fuel in main tank
            remainingFuel -= 5; // Subtract 5 liters of fuel from main tank
            
            if (additionalTank >= 1) { // If there is at least 1 liter of fuel in additional tank
                additionalTank -= 1; // Transfer 1 liter of fuel from additional tank to main tank
                remainingFuel += 1; // Increase the remaining fuel in main tank by 1
                distance += 10; // Add 10 km to the distance traveled
            }
        }
        
        return distance;
    }
}