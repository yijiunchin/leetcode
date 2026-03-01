class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        f1, f2, f3 = defaultdict(int), defaultdict(int), defaultdict(int)
        d1 = d2 = c3 = l1 = l2 = l3 = 0
        ans = 0
        for x in nums:
            if f1[x] == 0:
                d1 += 1

            f1[x] += 1
            while d1 > k:
                f1[nums[l1]] -= 1
                if f1[nums[l1]] == 0:
                    d1 -= 1

                l1 += 1

            if f2[x] == 0:
                d2 += 1

            f2[x] += 1
            while d2 >= k:
                f2[nums[l2]] -= 1
                if f2[nums[l2]] == 0:
                    d2 -= 1

                l2 += 1

            f3[x] += 1
            if f3[x] == m:
                c3 += 1

            while c3 >= k:
                f3[nums[l3]] -= 1
                if f3[nums[l3]] == m - 1:
                    c3 -= 1

                l3 += 1

            ans += max(0, min(l2, l3) - l1)

        return ans
