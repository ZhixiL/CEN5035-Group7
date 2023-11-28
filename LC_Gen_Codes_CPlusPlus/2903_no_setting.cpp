Here is the converted Java code:


import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findIndices(List<Integer> nums, int indexDifference, int valueDifference) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (Math.abs(i - j) >= indexDifference && Math.abs(nums.get(i) - nums.get(j)) >= valueDifference) {
                    List<Integer> result = new ArrayList<>();
                    result.add(i);
                    result.add(j);
                    return result;
                }
            }
        }
        return new ArrayList<Integer>(List.of(-1, -1));
    }
}