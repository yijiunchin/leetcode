class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        m = max(nums)
        spf = list(range(m + 1))
        for i in range(2, int(m**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, m + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        mp = defaultdict(list)
        for i, v in enumerate(nums):
            while v > 1:
                p = spf[v]
                mp[p].append(i)
                while v % p == 0:
                    v //= p

        q = deque([(0, 0)])
        seen_idx = [False] * n
        seen_idx[0] = True
        seen_p = [False] * (m + 1)

        while q:
            u, step = q.popleft()
            if u == n - 1:
                return step

            for nxt in (u - 1, u + 1):
                if 0 <= nxt < n and not seen_idx[nxt]:
                    seen_idx[nxt] = True
                    q.append((nxt, step + 1))

            val = nums[u]
            if val > 1 and spf[val] == val and not seen_p[val]:
                seen_p[val] = True
                for nxt in mp[val]:
                    if not seen_idx[nxt]:
                        seen_idx[nxt] = True
                        q.append((nxt, step + 1))
        
        return -1
