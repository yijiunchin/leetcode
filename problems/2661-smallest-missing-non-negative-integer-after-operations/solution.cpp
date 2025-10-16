class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        vector<int> times(value);
        int min_value = INT_MAX;
        int key = 0;
        
        for (const auto &i: nums) {
            ++times[(i % value + value) % value];
        }

        for (int i = 0; i < value; ++i) {
            if (times[i] < min_value) {
                key = i;
                min_value = times[i];
            }
        }

        return key + (min_value * value);
    }
};
