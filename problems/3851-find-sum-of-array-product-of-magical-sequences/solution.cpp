class Solution {
public:
    int magicalSum(int m, int k, vector<int>& nums) {
        const int MOD = 1'000'000'007;
        int n = (int)nums.size();
        auto modpow = [&](long long a, long long e){
            long long r = 1;
            a %= MOD;
            while (e) {
                if (e & 1) r = (r * a) % MOD;
                a = (a * a) % MOD;
                e >>= 1;
            }
            return r;
        };
        auto inv = [&](long long x){ return modpow((x%MOD+MOD)%MOD, MOD - 2); };

        vector<long long> fact(m+1, 1), invfact(m+1, 1);
        for (int i = 1; i <= m; ++i) fact[i] = fact[i-1] * i % MOD;
        invfact[m] = inv(fact[m]);
        for (int i = m; i >= 1; --i) invfact[i-1] = invfact[i] * i % MOD;

        vector<vector<long long>> w(n, vector<long long>(m+1, 0));
        for (int j = 0; j < n; ++j) {
            w[j][0] = 1;
            long long p = 1;
            for (int t = 1; t <= m; ++t) {
                p = (p * nums[j]) % MOD;
                w[j][t] = p * invfact[t] % MOD;
            }
        }

        int M = m;
        int Kcap = min(k, m);

        vector<vector<vector<long long>>> dp_cur(M+1, vector<vector<long long>>(M+1, vector<long long>(Kcap+1, 0)));
        dp_cur[0][0][0] = 1;

        for (int j = 0; j < n; ++j) {
            vector<vector<vector<long long>>> dp_next(M+1, vector<vector<long long>>(M+1, vector<long long>(Kcap+1, 0)));
            for (int carry = 0; carry <= M; ++carry) {
                for (int used = 0; used <= M; ++used) {
                    for (int ones = 0; ones <= Kcap; ++ones) {
                        long long curv = dp_cur[carry][used][ones];
                        if (curv == 0) continue;
                        int max_t = M - used;
                        for (int t = 0; t <= max_t; ++t) {
                            int total = carry + t;
                            int bit = total & 1;
                            int new_ones = ones + bit;
                            if (new_ones > Kcap) continue;
                            int new_carry = total >> 1;
                            int new_used = used + t;
                            long long add = (curv * w[j][t]) % MOD;
                            dp_next[new_carry][new_used][new_ones] += add;
                            if (dp_next[new_carry][new_used][new_ones] >= MOD)
                                dp_next[new_carry][new_used][new_ones] -= MOD;
                        }
                    }
                }
            }
            dp_cur.swap(dp_next);
        }

        long long inner_sum = 0;
        for (int carry = 0; carry <= M; ++carry) {
            int carry_pop = __builtin_popcount((unsigned)carry);
            for (int ones = 0; ones <= Kcap; ++ones) {
                if (ones + carry_pop != k) continue;
                inner_sum += dp_cur[carry][m][ones];
                if (inner_sum >= MOD) inner_sum -= MOD;
            }
        }

        long long ans = (inner_sum * fact[m]) % MOD;
        return (int)ans;
    }
};
