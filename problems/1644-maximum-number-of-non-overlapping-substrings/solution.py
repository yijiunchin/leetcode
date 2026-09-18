class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        fst = {c: s.index(c) for c in set(s)}
        lst = {c: s.rindex(c) for c in set(s)}
        ivs = []
        for l in fst.values():
            r, i = lst[s[l]], l
            while i <= r and fst[s[i]] >= l:
                r = max(r, lst[s[i]])
                i += 1
            if i > r:
                ivs.append((r, l))
        res, end = [], -1
        for r, l in sorted(ivs):
            if l > end:
                res.append(s[l : r + 1])
                end = r
        return res
