class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @cache
        def dp(i: int) -> int:
            res = 1
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dp(j))
                
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dp(j))
                
            return res

        return max(dp(i) for i in range(n))
