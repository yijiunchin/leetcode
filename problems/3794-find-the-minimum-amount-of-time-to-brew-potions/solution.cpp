#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        int skill_size = skill.size();
        int mana_size = mana.size();
        vector<uint64_t> dp(skill_size, 0);

        for (int j = 0; j < mana_size; ++j) {
            uint64_t prev = 0;
            for (int i = 0; i < skill_size; ++i) {
                dp[i] = max(dp[i], prev) + skill[i] * mana[j];
                prev = dp[i];
            }

            for (int i = skill_size - 1; i > 0; --i) {
                dp[i - 1] = dp[i] - mana[j] * skill[i];
            }
        }

        return dp.back();
    }
};
