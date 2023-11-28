c++
class Solution {
public:
    bool isGood(vector<int>& nums) {
        int n = *max_element(nums.begin(), nums.end()); // get the maximum element in the vector
        vector<int> base(n);
        for (int i = 0; i < n; i++) {
            base[i] = i + 1;
        }
        base.push_back(n);
        
        sort(nums.begin(), nums.end()); // sort the nums vector
        
        return nums == base; // check if nums is equal to base vector
    }
};