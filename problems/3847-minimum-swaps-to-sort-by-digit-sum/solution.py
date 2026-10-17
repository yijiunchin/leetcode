class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(
            range(n), key=lambda i: (sum(int(d) for d in str(nums[i])), nums[i])
        )
        vis = [False] * n
        ans = 0
        for i in range(n):
            if not vis[i]:
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = arr[j]
                    ans += 1
                ans -= 1
        return ans
