class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for row in boxGrid:
            empty = len(row) - 1
            for j in range(len(row) - 1, -1, -1):
                if row[j] == '*':
                    empty = j - 1
                elif row[j] == '#':
                    row[j], row[empty] = '.', '#'
                    empty -= 1
        return [list(r) for r in zip(*boxGrid[::-1])]
