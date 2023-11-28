cpp
class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<pair<string, int>> people;
        
        // Create a vector of pairs (name, height)
        for (int i = 0; i < names.size(); i++) {
            people.push_back(make_pair(names[i], heights[i]));
        }
        
        // Sort the vector of pairs by height in descending order
        sort(people.begin(), people.end(), [](const pair<string, int>& a, const pair<string, int>& b) {
            return a.second > b.second;
        });
        
        // Extract the names from the sorted vector of pairs
        vector<string> sorted_names;
        for (const auto& pair : people) {
            sorted_names.push_back(pair.first);
        }
        
        return sorted_names;
    }
};