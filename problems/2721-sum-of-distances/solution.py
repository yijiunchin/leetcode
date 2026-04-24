class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
            
        ans = [0] * len(nums)
        for idx in pos.values():
            k = len(idx)
            s = sum(idx) - k * idx[0]
            for i in range(k):
                if i > 0:
                    s += (idx[i] - idx[i - 1]) * (2 * i - k)
                ans[idx[i]] = s
                
        return ans
