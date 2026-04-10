class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)
            
        res = [
            2 * (idx[i+2] - idx[i])
            for idx in pos.values() if len(idx) >= 3
            for i in range(len(idx) - 2)
        ]
        
        return min(res) if res else -1
