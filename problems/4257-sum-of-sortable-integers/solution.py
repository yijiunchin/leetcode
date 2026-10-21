class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        pref = [0, *accumulate(x > y for x, y in zip(nums, nums[1:]))]
        s = sorted(nums)

        def check(k: int) -> bool:
            for i in range(0, n, k):
                if s[i] != s[i + k - 1]:
                    drops = pref[i + k - 1] - pref[i]
                    if drops + (nums[i + k - 1] > nums[i]) != 1:
                        return False
                if (
                    min(nums[i : i + k]) != s[i]
                    or max(nums[i : i + k]) != s[i + k - 1]
                ):
                    return False
            return True

        return sum(k for k in range(1, n + 1) if n % k == 0 and check(k))
