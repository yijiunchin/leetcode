class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        nns = []
        ans = []
        for i, n in enumerate(nums):
            if n >= 0:
                nns.append(n)

        if not nns:
            return nums

        k = k % len(nns)
        nns = nns + nns[:k]
        count = 0

        for i, n in enumerate(nums):
            if n >= 0:
                ans.append(nns[k + count])
                count += 1
            else:
                ans.append(n)
        
        return ans

