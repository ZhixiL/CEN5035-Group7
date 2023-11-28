import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int numberOfPoints(List<List<Integer>> nums) {
        Set<Integer> coveredPoints = new HashSet<>();
        
        for (List<Integer> car : nums) {
            int start = car.get(0);
            int end = car.get(1);
            
            for (int point = start; point <= end; point++) {
                coveredPoints.add(point);
            }
        }
        
        return coveredPoints.size();
    }
}