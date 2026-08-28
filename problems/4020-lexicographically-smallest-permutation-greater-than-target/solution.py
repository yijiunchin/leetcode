class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        m = 0
        while m < len(s) and cnt[target[m]]:
            cnt[target[m]] -= 1
            m += 1
        for i in range(min(len(s) - 1, m), -1, -1):
            if i < m:
                cnt[target[i]] += 1
            for c in sorted(cnt):
                if c > target[i] and cnt[c]:
                    cnt[c] -= 1
                    return target[:i] + c + ''.join(sorted(cnt.elements()))
        return ''
