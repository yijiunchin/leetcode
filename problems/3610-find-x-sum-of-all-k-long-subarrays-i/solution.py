class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ret = []
        for i in range(len(nums) - k + 1):
            ans = 0
            for k_, v in sorted(Counter(nums[i:i+k]).most_common(), key=lambda x_: (x_[1], x_[0]), reverse=True)[:x]:
                ans += k_ * v

            ret.append(ans)
        return ret
           
