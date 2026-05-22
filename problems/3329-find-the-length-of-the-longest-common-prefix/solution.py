class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen = set()
        for x in arr1:
            while x and x not in seen:
                seen.add(x)
                x //= 10
                
        ans = 0
        for y in arr2:
            while y and y not in seen:
                y //= 10
            if y:
                ans = max(ans, len(str(y)))
                
        return ans
