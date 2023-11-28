class Solution {
public:
    int countSymmetricIntegers(int low, int high) {
        int count = 0;
        
        for (int i = low; i <= high; i++) {
            string num_str = to_string(i);
            
            if (num_str.length() % 2 != 0) {
                continue;
            }
            
            int n = num_str.length() / 2;
            
            int first_sum = 0;
            for (int j = 0; j < n; j++) {
                first_sum += num_str[j] - '0';
            }
            
            int second_sum = 0;
            for (int j = n; j < num_str.length(); j++) {
                second_sum += num_str[j] - '0';
            }
            
            if (first_sum == second_sum) {
                count++;
            }
        }
        
        return count;
    }
};