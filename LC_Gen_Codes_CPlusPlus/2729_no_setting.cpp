class Solution {
public:
    bool isFascinating(int n) {
        // Concatenate n with 2*n and 3*n
        string concat = to_string(n) + to_string(2 * n) + to_string(3 * n);

        // Count the occurrences of each digit in the concatenated number
        vector<int> digit_counts(10, 0);
        for (char digit : concat) {
            digit_counts[digit - '0']++;
        }

        // Check if all digits from 1 to 9 occur exactly once and there are no zeros
        for (int i = 1; i < 10; i++) {
            if (digit_counts[i] != 1) {
                return false;
            }
        }
        if (digit_counts[0] != 0) {
            return false;
        }

        return true;
    }
};