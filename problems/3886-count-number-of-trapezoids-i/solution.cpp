class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        unordered_map<int, int> pointNum;
        uint64_t ans = 0, sum = 0;
        for (const auto& point : points) {
            ++pointNum[point[1]];
        }
        
        for (const auto& [_, pNum] : pointNum) {
            uint64_t edge = (uint64_t)pNum * (pNum - 1) / 2;
            ans += edge * sum;
            sum += edge;
        }

        return ans % (int)(1e9 + 7);
    }
};
