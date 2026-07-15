class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)
        return gcd(n * n, n * (n + 1))
