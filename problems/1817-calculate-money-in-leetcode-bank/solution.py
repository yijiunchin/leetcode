class Solution:
    def totalMoney(self, n: int) -> int:
        index = n // 7
        high = (index if index == 0 else index - 1)
        return 28 * index + 7 * (1 + high) * high // 2 + sum(1 + index + i for i in range(n % 7))

