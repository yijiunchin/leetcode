class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        pool = ''.join(map(str, digits))
        return sum(
            all(str(n).count(c) <= pool.count(c) for c in str(n))
            for n in range(100, 1000, 2)
        )
