class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        idle = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(idle)
        busy = []
        ans = []
        t = 0
        for j, task in enumerate(tasks):
            t = max(t, j)
            if not idle and busy and busy[0][0] > t:
                t = busy[0][0]
            while busy and busy[0][0] <= t:
                heapq.heappush(idle, heapq.heappop(busy)[1:])
            w, i = heapq.heappop(idle)
            ans.append(i)
            heapq.heappush(busy, (t + task, w, i))
        return ans
