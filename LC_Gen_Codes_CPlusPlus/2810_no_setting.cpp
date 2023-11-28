c++
#include <string>
#include <stack>

class Solution {
public:
    std::string finalString(std::string s) {
        std::string result = "";
        std::stack<char> stack;
        for (char c : s) {
            if (c == 'i') {
                while (!stack.empty()) {
                    result += stack.top();
                    stack.pop();
                }
            } else {
                stack.push(c);
            }
        }
        while (!stack.empty()) {
            result += stack.top();
            stack.pop();
        }
        return result;
    }
};