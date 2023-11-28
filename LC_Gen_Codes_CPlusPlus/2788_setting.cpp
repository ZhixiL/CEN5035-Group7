Here is the equivalent implementation of the `splitWordsBySeparator()` function in C++:

cpp
class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> result;
        for (string word : words) {
          stringstream ss(word);
          string split;
          while (getline(ss, split, separator)) {
            if (split != "") {
              result.push_back(split);
            }
          }
        }
        return result;
    }
};