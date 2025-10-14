class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        if (k == 1) {
            return true;
        }
        int num_size = nums.size();
        vector<int> valid(num_size, 1);

        for (int i = 1; i < num_size; ++i) {
            if (nums[i - 1] < nums[i]) {
                valid[i] = valid[i - 1] + 1;
            }
        }

        for (int i = 1; i < num_size - k; ++i) {
            if (valid[i] >= k && valid[i + k] >= k) {
                return true;
            }
        }
        
        return false;
    }
};

