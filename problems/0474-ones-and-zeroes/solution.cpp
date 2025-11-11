class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int16_t len = strs.size();
        vector<vector<int16_t>> dp(m + 1, vector<int16_t>(n + 1, 0));
        for (const auto& str: strs) {
            uint8_t zero_count = 0, one_count = 0;
            for (const auto chr: str)
                (chr == '0' ? zero_count : one_count) += 1;
            for (int16_t i = m; i >= zero_count; --i)
                for (int16_t j = n; j >= one_count; --j) 
                    dp[i][j] = max(dp[i][j], static_cast<int16_t>(1 + dp[i - zero_count][j - one_count]));
        }
        return dp[m][n];
    }
};
