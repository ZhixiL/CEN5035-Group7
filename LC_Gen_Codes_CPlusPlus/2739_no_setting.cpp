class Solution {
public:
    int distanceTraveled(int mainTank, int additionalTank) {
        int distance = mainTank * 10;
        int remainingFuel = mainTank;

        while (remainingFuel >= 5) {
            remainingFuel -= 5;

            if (additionalTank >= 1) {
                additionalTank -= 1;
                remainingFuel += 1;
                distance += 10;
            }
        }
        
        return distance;
    }
};