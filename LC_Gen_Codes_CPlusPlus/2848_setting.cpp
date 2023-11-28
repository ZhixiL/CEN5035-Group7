class Solution {
    public:
        int numberOfPoints(vector<vector<int>>& nums) {
            unordered_set<int> covered_points;
            
            for (auto car : nums) {
                int start = car[0];
                int end = car[1];
                
                for (int point = start; point <= end; point++) {
                    covered_points.insert(point);
                }
            }
        
            return covered_points.size();
        }
    };