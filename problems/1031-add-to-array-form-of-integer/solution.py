class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(10000)
        return [int(n) for n in str(int(''.join([str(n) for n in num])) + k)]
