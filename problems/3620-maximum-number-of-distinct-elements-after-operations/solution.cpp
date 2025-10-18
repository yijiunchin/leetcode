class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        if (nums.empty()) return 0;
        ranges::sort(nums);

        int next_free = -INT_MAX;
        int ans = 0;
        for (auto i : nums) {
            int place = max(next_free, i - k);
            if (place <= i + k) {
                ++ans;
                next_free = place + 1;
            }
        }
        return ans;
    }
};
