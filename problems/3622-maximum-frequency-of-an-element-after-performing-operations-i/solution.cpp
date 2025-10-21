class Solution
{
public:
    int maxFrequency(vector<int> &nums, int k, int numOperations)
    {
        int n = nums.size();
        int min_num = *min_element(nums.begin(), nums.end()),
            max_num = *max_element(nums.begin(), nums.end());
        int m = max_num - min_num + 1;
        const auto key = [min_num](int num)
        {
            return num - min_num;
        };

        vector<int> freq(m, 0);
        for (auto num : nums)
            freq[key(num)] += 1;
        vector<int> prefix(m + 1);
        prefix[0] = 0;
        for (int i = 0; i < m; ++i)
            prefix[i + 1] = prefix[i] + freq[i];
        const auto get_count = [&prefix, &key, k, m](int left, int right)
        {
            if (right < left)
                return 0;
            return prefix[min(m, key(right + 1))] - prefix[max(0, key(left))];
        };

        int result = 0;
        for (int i = min_num; i <= max_num; ++i)
            result = max(result, freq[key(i)] + min(numOperations, get_count(i - k, i + k) - freq[key(i)]));
        return result;
    }
};

