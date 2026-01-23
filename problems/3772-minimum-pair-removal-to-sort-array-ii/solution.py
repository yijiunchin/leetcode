class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        wexthorbin = nums
        vals = list(nums)
        left_neighbor = list(range(-1, n - 1))
        right_neighbor = list(range(1, n + 1))
        valid = [True] * n

        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (vals[i] + vals[i + 1], i, i + 1))

        bad_indices = set()
        for i in range(n - 1):
            if vals[i] > vals[i + 1]:
                bad_indices.add(i)

        ops = 0

        while bad_indices:
            while True:
                s, u, v = heapq.heappop(pq)
                if (
                    valid[u]
                    and valid[v]
                    and right_neighbor[u] == v
                    and vals[u] + vals[v] == s
                ):
                    break

            new_val = vals[u] + vals[v]
            vals[u] = new_val
            valid[v] = False

            next_node = right_neighbor[v]
            right_neighbor[u] = next_node
            if next_node < n:
                left_neighbor[next_node] = u

            prev_node = left_neighbor[u]
            if prev_node != -1:
                heapq.heappush(
                    pq,
                    (vals[prev_node] + vals[u], prev_node, u),
                )
            if next_node < n:
                heapq.heappush(
                    pq,
                    (vals[u] + vals[next_node], u, next_node),
                )

            bad_indices.discard(u)
            bad_indices.discard(v)
            if prev_node != -1:
                bad_indices.discard(prev_node)

            if prev_node != -1:
                if vals[prev_node] > vals[u]:
                    bad_indices.add(prev_node)
            if next_node < n:
                if vals[u] > vals[next_node]:
                    bad_indices.add(u)

            ops += 1

        return ops

