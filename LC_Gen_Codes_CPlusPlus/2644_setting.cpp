class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        vector<int> score(divisors.size(), 0); // initialize score array with zeros
        for (int num : nums) {
            for (int i = 0; i < divisors.size(); i++) {
                if (num % divisors[i] == 0) {
                    score[i] += 1; // increment the score if num is divisible by divisor
                }
            }
        }
        int max_score = *max_element(score.begin(), score.end()); // find the maximum score
        vector<int> max_score_divisors;
        for (int i = 0; i < score.size(); i++) {
            if (score[i] == max_score) {
                max_score_divisors.push_back(divisors[i]);
            }
        }
        return *min_element(max_score_divisors.begin(), max_score_divisors.end()); // return the minimum of the divisors with maximum score
    }
};