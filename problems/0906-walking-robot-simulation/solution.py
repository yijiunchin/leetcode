class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        obs = set(map(tuple, obstacles))
        x = y = d = max_d2 = 0
        
        for cmd in commands:
            if cmd == -2:
                d = (d - 1) % 4
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obs:
                        break
                    x, y = x + dx, y + dy
                max_d2 = max(max_d2, x * x + y * y)
                
        return max_d2
