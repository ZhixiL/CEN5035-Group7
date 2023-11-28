cpp
#include <iostream>

class Solution {
public:
    int sumOfMultiples(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                sum += i;
            }
        }
        return sum;
    }
};

int main() {
    Solution solution;
    std::cout << solution.sumOfMultiples(7) << std::endl;  // Output: 21
    std::cout << solution.sumOfMultiples(10) << std::endl;  // Output: 40
    std::cout << solution.sumOfMultiples(9) << std::endl;  // Output: 30
    return 0;
}