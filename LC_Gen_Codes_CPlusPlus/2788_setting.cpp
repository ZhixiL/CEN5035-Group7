class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> result;
        for (string word : words) {
            vector<string> splits = split(word, separator);
            for (string split : splits) {
                if (split != "") {
                    result.push_back(split);
                }
            }
        }
        return result;
    }
    
    vector<string> split(string word, char separator) {
        stringstream ss(word);
        string substring;
        vector<string> splits;
        while (getline(ss, substring, separator)) {
            splits.push_back(substring);
        }
        return splits;
    }
};