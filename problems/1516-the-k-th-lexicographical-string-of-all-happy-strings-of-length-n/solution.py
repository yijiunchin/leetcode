class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ""
        
        k -= 1
        q, k = divmod(k, 1 << (n - 1))
        res = ["abc"[q]]
        
        for i in range(n - 2, -1, -1):
            choices = [c for c in "abc" if c != res[-1]]
            q, k = divmod(k, 1 << i)
            res.append(choices[q])
            
        return "".join(res)
