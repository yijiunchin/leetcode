class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        bit = [0] * (2 * n + 2)
        
        def add(i: int) -> None:
            while i < len(bit):
                bit[i] += 1
                i += i & -i
                
        def query(i: int) -> int:
            s = 0
            while i:
                s += bit[i]
                i &= i - 1
            return s
            
        ans = curr = 0
        add(n + 1)
        
        for num in nums:
            curr += 1 if num == target else -1
            ans += query(curr + n)
            add(curr + n + 1)
            
        return ans
