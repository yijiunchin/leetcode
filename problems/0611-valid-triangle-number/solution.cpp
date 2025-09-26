class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        size_t n = nums.size();
        if (n < 3) return 0;

        ranges::sort(nums);
        int result = 0;

        for (size_t i = n - 1; i >= 2; --i) {
            if (nums[i] == 0) continue;
            size_t left = 0, right = i - 1;
            while (left < right) {
                if (nums[left] + nums[right] > nums[i]) {
                    result += (right - left);
                    --right;
                } else {
                    ++left;
                }
            }
        }
        return result;
    }
};

