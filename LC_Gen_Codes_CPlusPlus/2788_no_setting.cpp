Here is the C++ implementation of the provided code:

cpp
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
    
private:
    vector<string> split(string word, char separator) {
        vector<string> splits;
        string current;
        for (char c : word) {
            if (c == separator) {
                if (!current.empty()) {
                    splits.push_back(current);
                    current.clear();
                }
            } else {
                current += c;
            }
        }
        if (!current.empty()) {
            splits.push_back(current);
        }
        return splits;
    }
};


Note that I added a helper function `split` to split each word by the provided separator character. This function takes a string `word` and a character `separator` and returns a vector of strings containing the splits.