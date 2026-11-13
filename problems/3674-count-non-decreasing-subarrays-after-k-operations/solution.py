class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        dq = deque()
        ans = cost = 0
        R = len(nums) - 1
        
        for L in range(len(nums) - 1, -1, -1):
            count = 1
            val = nums[L]
            
            while dq and dq[0][0] <= val:
                prev_val, prev_count = dq.popleft()
                cost += (val - prev_val) * prev_count
                count += prev_count
            dq.appendleft([val, count])
            
            while cost > k:
                cost -= dq[-1][0] - nums[R]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                R -= 1
                
            ans += R - L + 1
            
        return ans
