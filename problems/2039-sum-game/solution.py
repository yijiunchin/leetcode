class Solution:
    def sumGame(self, num: str) -> bool:
        h = len(num) // 2
        l, r = num[:h], num[h:]
        s1 = sum(int(c) for c in l if c != '?')
        s2 = sum(int(c) for c in r if c != '?')
        q1, q2 = l.count('?'), r.count('?')
        return (q1 + q2) % 2 != 0 or (s1 - s2) * 2 != (q2 - q1) * 9
