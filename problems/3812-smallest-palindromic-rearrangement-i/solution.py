class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        left = ''.join(k * (v // 2) for k, v in sorted(cnt.items()))
        mid = next((k for k, v in cnt.items() if v % 2), '')
        return left + mid + left[::-1]
