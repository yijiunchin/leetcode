class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        suf_sum = 0
        suf_min = float('inf')
        score = -float('inf')
        for i in range(len(nums) - 1, 0, -1):
            value = nums[i]
            suf_sum += value
            if value < suf_min: suf_min = value
            current_score = nums_sum - suf_sum - suf_min
            if current_score > score: score = current_score

        return score
