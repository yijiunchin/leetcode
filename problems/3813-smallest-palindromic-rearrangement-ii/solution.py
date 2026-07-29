class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        mid = ''.join(char for char, count in freq.items() if count % 2)
        half = []
        for char in sorted(freq):
            half.extend([char] * (freq[char] // 2))
            
        half_freq = Counter(half)
        length = len(half)
        perms = math.factorial(length)
        for count in half_freq.values():
            perms //= math.factorial(count)
            
        if k > perms:
            return ''
            
        k -= 1
        res = []
        for _ in range(length):
            for i in range(26):
                char = chr(97 + i)
                if half_freq[char]:
                    ways = perms * half_freq[char] // length
                    if k < ways:
                        res.append(char)
                        half_freq[char] -= 1
                        perms = ways
                        length -= 1
                        break
                    k -= ways
                    
        ans = ''.join(res)
        return f'{ans}{mid}{ans[::-1]}'
