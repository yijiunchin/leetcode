class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        arr = list(s)
        pre = [0] * (4 * n)
        suf = [0] * (4 * n)
        mx = [0] * (4 * n)

        def maintain(o: int, l: int, r: int) -> None:
            lc, rc, mid = o * 2, o * 2 + 1, (l + r) // 2
            pre[o], suf[o] = pre[lc], suf[rc]
            match = arr[mid] == arr[mid + 1]
            
            mx[o] = max(mx[lc], mx[rc], suf[lc] + pre[rc] if match else 0)
            
            if match:
                if pre[lc] == mid - l + 1:
                    pre[o] += pre[rc]
                if suf[rc] == r - mid:
                    suf[o] += suf[lc]

        def build(o: int, l: int, r: int) -> None:
            if l == r:
                pre[o] = suf[o] = mx[o] = 1
                return
            mid = (l + r) // 2
            build(o * 2, l, mid)
            build(o * 2 + 1, mid + 1, r)
            maintain(o, l, r)

        def update(o: int, l: int, r: int, idx: int) -> None:
            if l == r:
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(o * 2, l, mid, idx)
            else:
                update(o * 2 + 1, mid + 1, r, idx)
            maintain(o, l, r)

        build(1, 0, n - 1)
        ans = []
        for i, c in zip(queryIndices, queryCharacters):
            if arr[i] != c:
                arr[i] = c
                update(1, 0, n - 1, i)
            ans.append(mx[1])
            
        return ans
