class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = Counter(x for i in range(len(nums) - k + 1) for x in set(nums[i : i + k]))
        return max([x for x, c in freq.items() if c == 1], default=-1)
