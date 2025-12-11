from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_min = {}
        row_max = {}
        col_min = {}
        col_max = {}
        
        for x, y in buildings:
            if x not in row_min:
                row_min[x] = y
                row_max[x] = y
            else:
                if y < row_min[x]:
                    row_min[x] = y
                if y > row_max[x]:
                    row_max[x] = y
            
            if y not in col_min:
                col_min[y] = x
                col_max[y] = x
            else:
                if x < col_min[y]:
                    col_min[y] = x
                if x > col_max[y]:
                    col_max[y] = x
        
        count = 0
        
        for x, y in buildings:
            is_horizontally_covered = row_min[x] < y < row_max[x]
            
            if not is_horizontally_covered:
                continue
                
            is_vertically_covered = col_min[y] < x < col_max[y]
            
            if is_vertically_covered:
                count += 1
                
        return count

