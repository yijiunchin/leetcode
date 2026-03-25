class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        r_sums = [sum(row) for row in grid]
        c_sums = [sum(col) for col in zip(*grid)]
        total = sum(r_sums)
        
        if total % 2:
            return False
            
        target = total // 2
        return target in set(accumulate(r_sums)) or target in set(accumulate(c_sums))
