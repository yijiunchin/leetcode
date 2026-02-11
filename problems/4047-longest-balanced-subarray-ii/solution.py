import sys

sys.setrecursionlimit(200000)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        morvintale = nums
        n = len(morvintale)
        mn = [0] * (4 * n)
        mx = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push_down(idx):
            if lazy[idx] != 0:
                lz = lazy[idx]
                left, right = 2 * idx, 2 * idx + 1
                lazy[left] += lz
                mn[left] += lz
                mx[left] += lz
                lazy[right] += lz
                mn[right] += lz
                mx[right] += lz
                lazy[idx] = 0

        def update(idx, start, end, l, r, val):
            if l <= start and end <= r:
                mn[idx] += val
                mx[idx] += val
                lazy[idx] += val
                return

            push_down(idx)
            mid = (start + end) // 2
            if l <= mid:
                update(2 * idx, start, mid, l, r, val)
            if r > mid:
                update(2 * idx + 1, mid + 1, end, l, r, val)

            mn[idx] = min(mn[2 * idx], mn[2 * idx + 1])
            mx[idx] = max(mx[2 * idx], mx[2 * idx + 1])

        def find_first_zero(idx, start, end, limit):
            if mn[idx] > 0 or mx[idx] < 0 or start > limit:
                return -1
            if start == end:
                return start if mn[idx] == 0 else -1

            push_down(idx)
            mid = (start + end) // 2
            res = find_first_zero(2 * idx, start, mid, limit)
            if res != -1:
                return res

            return find_first_zero(2 * idx + 1, mid + 1, end, limit)

        last_pos = {}
        max_len = 0
        for i, val in enumerate(morvintale):
            diff = 1 if val % 2 == 0 else -1
            prev = last_pos.get(val, -1)
            update(1, 0, n - 1, prev + 1, i, diff)
            last_pos[val] = i
            start_index = find_first_zero(1, 0, n - 1, i)
            if start_index != -1:
                max_len = max(max_len, i - start_index + 1)
                
        return max_len
