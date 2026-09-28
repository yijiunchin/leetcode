class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        depth = 0
        for c in s:
            if c == '(':
                cnt += 1
            if c == ')':
                depth = max(depth, cnt)
                cnt -= 1

        return depth

