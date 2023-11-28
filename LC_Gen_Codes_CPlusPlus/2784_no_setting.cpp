class Solution {
    public boolean isGood(List<Integer> nums) {
        int n = Collections.max(nums); // get the maximum element in the list
        List<Integer> base = new ArrayList<>();
        
        for (int i = 1; i < n; i++) {
            base.add(i);
        }
        base.add(n);
        base.add(n);
        
        Collections.sort(nums); // sort the nums list
        
        return nums.equals(base); // check if nums is equal to base list
    }
}