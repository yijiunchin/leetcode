class Solution {
public:
    long long sumAndMultiply(int n) {
        int64_t ans = 0;
        int64_t sum = 0;
        int cnt = 0;
        while (n > 0) {
            if (n % 10 == 0) {
                n /= 10;
                continue;
            }
            sum += n % 10;
            ans += (n % 10) * pow(10, cnt++); 
            n /= 10;
        }
        return ans * sum;
    }
};
