class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        return all(row[j] == row[(j + k) % n] for row in mat for j in range(n))
