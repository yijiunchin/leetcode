class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = [i.count('1') for i in bank if '1' in i]
        ans = 0
        for i in range(len(n) - 1):
            ans += n[i] * n[i + 1]
        
        return ans
