class Solution:
    def numSteps(self, s: str) -> int:
        steps = carry = 0
        for char in reversed(s[1:]):
            if int(char) + carry == 1:
                carry = 1
                steps += 2
            else:
                steps += 1
        return steps + carry
