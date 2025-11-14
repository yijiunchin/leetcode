class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        vector<vector<int16_t>> diff(n, vector<int16_t>(n, 0));
        for (const auto& query: queries) {
            for (int16_t x = query[0]; x <= query[2]; ++x) {
                diff[x][query[1]] += 1;
                if(x + (query[3] + 1) / n < n)
                    diff[x + (query[3] + 1) / n][(query[3] + 1) % n] -= 1;
            }
        }
        int16_t acc = 0;
        vector<vector<int>> result(n, vector<int>(n, 0));
        for (int16_t x = 0; x < n; ++x) {
            for (int16_t y = 0; y < n; ++y) {
                acc += diff[x][y];
                result[x][y] = acc;
            }
        }
        return result;
    }
};
