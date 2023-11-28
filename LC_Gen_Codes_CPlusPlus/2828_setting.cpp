c++
#include <vector>
#include <string>

class Solution {
public:
    bool isAcronym(std::vector<std::string>& words, std::string s) {
        std::string acronym = "";
        for (std::string word : words) {
            acronym += word[0];
        }
        return acronym == s;
    }
};