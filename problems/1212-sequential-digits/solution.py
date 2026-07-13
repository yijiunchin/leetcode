class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        return sorted(
            int(s[i : i + L])
            for L in range(len(str(low)), len(str(high)) + 1)
            for i in range(10 - L)
            if low <= int(s[i : i + L]) <= high
        )
