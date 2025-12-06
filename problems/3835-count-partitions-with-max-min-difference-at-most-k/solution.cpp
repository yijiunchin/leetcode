class Solution {
public:
    int countPartitions(vector<int>& nums, int K) {
        int n = nums.size();
        if (n == 0) return 0;
        
        const int MOD =1e9+7;
        
        vector<long long> f(n+1, 0);
        vector<long long> g(n+1, 0);

        g[0] = 1; 

        deque<int> max_dq; 

        deque<int> min_dq; 
        int j = 1; 
        
        for (int i=1;i<=n;++i) {
            int current_idx =i-1; 
            int current_val =nums[current_idx]; 
            
            while (!max_dq.empty() && nums[max_dq.back()] <= current_val) {
                max_dq.pop_back();
            }
            max_dq.push_back(current_idx);

            while (!min_dq.empty() && nums[min_dq.back()] >= current_val) {
                min_dq.pop_back();
            }
            min_dq.push_back(current_idx);
            while (nums[max_dq.front()]-nums[min_dq.front()]>K) {
                if (max_dq.front() == j-1) {
                    max_dq.pop_front();
                }
                if (min_dq.front() == j-1) {
                    min_dq.pop_front();
                }
                j++;
            }
            long long prev_sum = (j-2>=0) ? g[j-2] :0;
            f[i] =(g[i-1]-prev_sum+MOD) % MOD;
            g[i] =(g[i-1]+f[i]) % MOD;
        }
        
        return f[n];
    }
};
