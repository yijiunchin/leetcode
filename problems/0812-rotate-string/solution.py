class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            if s[i:n] + s[0:i] == goal:
                return True

        return False
