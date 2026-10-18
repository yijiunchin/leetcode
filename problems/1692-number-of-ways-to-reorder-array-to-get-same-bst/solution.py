class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def dfs(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1
            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]
            ways = math.comb(len(left) + len(right), len(left))
            return ways * dfs(left) * dfs(right)
            
        return (dfs(nums) - 1) % (10**9 + 7)
