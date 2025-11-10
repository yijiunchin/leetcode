class Solution {
public:
    int minOperations(vector<int>& nums) {
        const int n = nums.size();
        vector<int> monotonic_stack;
        int result = 0;
        for (const auto num: nums) {
            while (not monotonic_stack.empty() and monotonic_stack.back() > num) {
                result += 1;
                monotonic_stack.pop_back();
            }
            if (monotonic_stack.empty() or monotonic_stack.back() != num)
                monotonic_stack.push_back(num);
        }

        int m = monotonic_stack.size();
        for (int left = 0, right = 1; left < m; left = right++) {
            while (right < m and monotonic_stack[left] == monotonic_stack[right])
                right += 1;
            if (monotonic_stack[left] != 0)
                result += 1;
        }
        return result;
    }
};
