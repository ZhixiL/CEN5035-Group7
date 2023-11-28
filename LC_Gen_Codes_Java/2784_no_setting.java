import java.util.Arrays;

class Solution {
    public boolean isGood(int[] nums) {
        int n = Arrays.stream(nums).max().getAsInt(); // get the maximum element in the array
        int[] base = new int[n];
        
        for (int i = 0; i < n - 1; i++) {
            base[i] = i + 1;
        }
        base[n-1] = n;
        
        Arrays.sort(nums); // sort the nums array
        
        return Arrays.equals(nums, base); // check if nums is equal to base array
    }
}