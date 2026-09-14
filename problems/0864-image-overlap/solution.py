class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        b = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]
        counts = Counter((br - ar, bc - ac) for ar, ac in a for br, bc in b)
        return max(counts.values(), default=0)
