Here is the converted code in C++:

cpp
class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        int count = 0;
        for (int hour : hours) {
            if (hour >= target) {
                count++;
            }
        }
        return count;
    }
};


Please note that the implementation is the same as the provided Python code. Only the syntax has been converted to C++.