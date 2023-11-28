java
class Solution {
    public int numberOfEmployeesWhoMetTarget(List<Integer> hours, int target) {
        int count = 0;
        for (int h : hours) {
            if (h >= target) {
                count += 1;
            }
        }
        return count;
    }
}