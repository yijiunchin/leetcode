class Solution {
public:
    int minOperations(vector<int>& nums) {
        int size = (int)nums.size();
        int zeros = ranges::count(nums, 1);
        if (zeros) return size - zeros;

        int loop = 0;
        while (loop < size - 1) {
            for (int i = 1; i < size - loop; ++i) {
                int common = gcd(nums[i - 1], nums[i]);
                if (common == 1) return size + loop;
                nums[i - 1] = common;
            }
            ++loop;
        }

        return -1;
    }
};
