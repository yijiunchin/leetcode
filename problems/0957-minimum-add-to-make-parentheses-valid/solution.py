class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0
        for char in s:
            if char == '(':
                right += 1
            elif right:
                right -= 1
            else:
                left += 1
        return left + right
