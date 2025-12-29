class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        adj = defaultdict(list)
        for pattern in allowed:
            adj[pattern[:2]].append(pattern[2])

        @lru_cache(None)
        def solve(current_bottom):
            if len(current_bottom) == 1:
                return True

            next_level_candidates = []

            def build_next_level(index, current_next):
                if index == len(current_bottom) - 1:
                    next_level_candidates.append(current_next)
                    return

                pair = current_bottom[index : index + 2]
                if pair in adj:
                    for top in adj[pair]:
                        build_next_level(index + 1, current_next + top)

            build_next_level(0, '')

            for nxt in next_level_candidates:
                if solve(nxt):
                    return True

            return False

        return solve(bottom)

