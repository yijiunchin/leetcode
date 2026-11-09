class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        reqs = [0] * k
        busy = []
        idle = list(range(k))
        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, node = heapq.heappop(busy)
                heapq.heappush(idle, i + (node - i) % k)
            while idle and idle[0] < i:
                v = heapq.heappop(idle)
                heapq.heappush(idle, i + (v - i) % k)
            if idle:
                node = heapq.heappop(idle) % k
                reqs[node] += 1
                heapq.heappush(busy, (a + l, node))
        mx = max(reqs)
        return [i for i, r in enumerate(reqs) if r == mx]
