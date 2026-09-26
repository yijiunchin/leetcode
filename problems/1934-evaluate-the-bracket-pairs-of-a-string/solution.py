class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        p = s.split('(')
        return p[0] + ''.join(
            d.get(k, '?') + v for k, v in (x.split(')') for x in p[1:])
        )
