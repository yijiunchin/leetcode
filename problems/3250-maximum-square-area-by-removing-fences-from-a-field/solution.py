class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: list[int], vFences: list[int]
    ) -> int:
        def get_all_distances(limit: int, fences: list[int]) -> set[int]:
            fences.extend([1, limit])
            fences.sort()
            dist_set = set()
            size = len(fences)
            for i in range(size):
                for j in range(i + 1, size):
                    dist_set.add(fences[j] - fences[i])
            return dist_set

        h_dists = get_all_distances(m, hFences)
        v_dists = get_all_distances(n, vFences)

        common_max = -1
        for d in h_dists:
            if d in v_dists:
                common_max = max(common_max, d)

        if common_max == -1:
            return -1
        
        return (common_max * common_max) % (10**9 + 7)

