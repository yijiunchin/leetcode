class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for n in arr1:
            ans += 1
            for m in arr2:
                if abs(n - m) <= d:
                    ans -= 1
                    break
        
        return ans
