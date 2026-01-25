class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        d = deque()
        for c in s:
            if d and c in mapping:
                if d[-1] == mapping.get(c):
                    d.pop()
                else:
                    return False
            else:
                d.append(c)

        return not d

