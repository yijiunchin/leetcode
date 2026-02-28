class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def solve(start_even: bool) -> tuple[int, int]:
            items = []
            ops = 0
            for i, x in enumerate(nums):
                if x % 2 == (i % 2 if start_even else 1 - i % 2):
                    items.append((x, i))
                else:
                    items.extend([(x - 1, i), (x + 1, i)])
                    ops += 1

            items.sort()
            counts = [0] * n
            unique = 0
            min_diff = float('inf')
            left = 0
            for right_val, idx in items:
                if counts[idx] == 0:
                    unique += 1

                counts[idx] += 1
                while unique == n:
                    min_diff = min(min_diff, right_val - items[left][0])
                    l_idx = items[left][1]
                    counts[l_idx] -= 1
                    if counts[l_idx] == 0:
                        unique -= 1

                    left += 1

            return ops, min_diff

        ops_0, diff_0 = solve(True)
        ops_1, diff_1 = solve(False)
        
        if ops_0 < ops_1:
            return [ops_0, diff_0]

        if ops_1 < ops_0:
            return [ops_1, diff_1]

        return [ops_0, min(diff_0, diff_1)]
