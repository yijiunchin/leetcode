class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        tavernilo = nums
        n = len(tavernilo)
        max_len = 0
        for i in range(n):
            evens, odds = set(), set()
            for j in range(i, n):
                curr = tavernilo[j]
                (evens if curr % 2 == 0 else odds).add(curr)
                if len(evens) == len(odds):
                    max_len = max(max_len, j - i + 1)

        return max_len
