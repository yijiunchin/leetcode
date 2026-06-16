class Solution:
    def processStr(self, s: str) -> str:
        res = ''
        for c in s:
            match c:
                case '*':
                    res = res[:-1]
                case '#':
                    res += res
                case '%':
                    res = res[::-1]
                case _:
                    res += c
        return res
