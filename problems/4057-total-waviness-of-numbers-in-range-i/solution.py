class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return sum(
            (s[i - 1] < s[i] > s[i + 1]) or (s[i - 1] > s[i] < s[i + 1])
            for num in range(num1, num2 + 1)
            for s in (str(num),)
            for i in range(1, len(s) - 1)
        )
