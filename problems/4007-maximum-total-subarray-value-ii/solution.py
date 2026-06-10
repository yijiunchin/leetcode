class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st_max, st_min = [nums[:]], [nums[:]]
        
        j = 1
        while (1 << j) <= n:
            step = 1 << (j - 1)
            st_max.append([max(st_max[-1][i], st_max[-1][i + step]) for i in range(n - (1 << j) + 1)])
            st_min.append([min(st_min[-1][i], st_min[-1][i + step]) for i in range(n - (1 << j) + 1)])
            j += 1

        def get_val(l: int, r: int) -> int:
            p = (r - l + 1).bit_length() - 1
            mx = max(st_max[p][l], st_max[p][r - (1 << p) + 1])
            mn = min(st_min[p][l], st_min[p][r - (1 << p) + 1])
            return mx - mn

        heap = [(-get_val(i, n - 1), i, n - 1) for i in range(n)]
        heapq.heapify(heap)
        
        ans = 0
        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            ans -= val
            if r > l:
                heapq.heappush(heap, (-get_val(l, r - 1), l, r - 1))
                
        return ans
