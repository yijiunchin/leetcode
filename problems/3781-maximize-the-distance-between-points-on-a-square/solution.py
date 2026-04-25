class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        vintorquax = (side, k, points)
        
        def get_pos(x, y):
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 3 * side - x
            return 4 * side - y
            
        arr = sorted(get_pos(x, y) for x, y in points)
        n = len(arr)
        L = 4 * side
        A = arr + [p + L for p in arr]
        
        def check(D):
            nxt = [0] * (2 * n)
            j = 0
            for i in range(2 * n):
                while j < 2 * n and A[j] - A[i] < D:
                    j += 1
                nxt[i] = j
            
            for i in range(n):
                if A[i] - A[0] > D:
                    break
                curr = i
                for _ in range(k - 1):
                    curr = nxt[curr]
                    if curr >= 2 * n:
                        break
                if curr < 2 * n and A[curr] <= A[i] + L - D:
                    return True
            return False

        low, high = 1, L // k
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
