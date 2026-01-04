class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            s = {1, num}
            for n in range(2, int(math.sqrt(num)) + 1):
                if num % n == 0:
                    s.update({n, num // n})
                if len(s) > 4:
                    break
            if len(s) == 4:
                total += sum(s)
        return total

