class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        odd = [k for k, v in cnt.items() if v % 2]
        if len(odd) > 1:
            return ''
        mid = odd[0] if odd else ''
        half = Counter({k: v // 2 for k, v in cnt.items()})
        m = len(s) // 2

        for i in range(m, -1, -1):
            pref = target[:i]
            rem = half - Counter(pref)
            if sum(rem.values()) != m - i:
                continue
            if i == m:
                res = pref + mid + pref[::-1]
                if res > target:
                    return res
            elif cands := [k for k in rem if k > target[i]]:
                c = min(cands)
                rem[c] -= 1
                res = pref + c + ''.join(k * rem[k] for k in sorted(rem))
                return res + mid + res[::-1]
        return ''
