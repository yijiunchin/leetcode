class Solution:
    def is_prime(self, n: int) -> bool:
        if n == 1: return False
        if n in (2, 3): return True
        if n % 2 == 0 or n % 3 == 0: return False
        for i in range(5, int(math.isqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def completePrime(self, num: int) -> bool:
        num_str = str(num)
        num_len = len(num_str)
        for i in range(num_len):
            if not self.is_prime(int(num_str[:num_len - i])):
                return False
            if not self.is_prime(int(num_str[i:])):
                return False
        return True

