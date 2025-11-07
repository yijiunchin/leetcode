long long powers[100000], buffer[100000];

class Solution {
public:
    long long maxPower(vector<int>& stations, int r, int k) {
        long long total = 0;
        int cities = stations.size();
        memset(powers, 0, sizeof(powers));
        for (int i = 0; i < cities; ++i) {
            total += stations[i];
            if (i > r)
                total -= stations[i - r - 1];
            powers[i] += total;
        }
        total = 0;
        for (int i = cities - 1; i >= 0; --i) {
            if (cities - i - 1 > r)
                total -= stations[i + r + 1];
            powers[i] += total;
            total += stations[i];
        }
        auto extrema = minmax_element(powers, powers + cities);
        long long lower = *extrema.first, upper = *extrema.second + k, middle, usage, sums;
        bool feasible;
        while (lower < upper) {
            middle = (lower + upper + 1) >> 1;
            memset(buffer, 0, sizeof(buffer));
            total = sums = 0;
            for (int i = 0; i < cities; ++i) {
                if (i > r)
                    total -= buffer[i - r - 1];
                if (powers[i] + total < middle) {
                    usage = (middle - (powers[i] + total));
                    buffer[min(i + r, cities - 1)] += usage;
                    total += usage;
                    sums += usage;
                }
            }
            if (sums > k)
                upper = middle - 1;
            else
                lower = middle;
        }
        return lower;
    }
};
