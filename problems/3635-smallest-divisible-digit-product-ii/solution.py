class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        a = b = c = d = 0
        while t % 2 == 0: a, t = a + 1, t // 2
        while t % 3 == 0: b, t = b + 1, t // 3
        while t % 5 == 0: c, t = c + 1, t // 5
        while t % 7 == 0: d, t = d + 1, t // 7
        if t > 1: return '-1'

        dp = [[''] * 31 for _ in range(48)]
        for i in range(48):
            for j in range(31):
                if i == 0 and j == 0: continue
                opts = []
                for digit, twos, threes in ((2,1,0), (3,0,1), (4,2,0), (6,1,1), (8,3,0), (9,0,2)):
                    ni, nj = max(0, i - twos), max(0, j - threes)
                    if ni == i and nj == j: continue
                    opts.append(''.join(sorted(dp[ni][nj] + str(digit))))
                dp[i][j] = min(opts, key=lambda x: (len(x), x)) if opts else ''

        fm = {'1': (0,0,0,0), '2': (1,0,0,0), '3': (0,1,0,0), '4': (2,0,0,0), 
              '5': (0,0,1,0), '6': (1,1,0,0), '7': (0,0,0,1), '8': (3,0,0,0), '9': (0,2,0,0)}

        z = num.find('0')
        z = len(num) if z == -1 else z
        
        p = [(0,0,0,0)]
        for ch in num[:z]:
            p.append(tuple(x + y for x, y in zip(p[-1], fm[ch])))

        if z == len(num) and all(x <= y for x, y in zip((a,b,c,d), p[-1])):
            return num

        for i in range(min(len(num) - 1, z), -1, -1):
            for digit in range(int(num[i]) + 1, 10):
                f = fm[str(digit)]
                ra = max(0, a - p[i][0] - f[0])
                rb = max(0, b - p[i][1] - f[1])
                rc = max(0, c - p[i][2] - f[2])
                rd = max(0, d - p[i][3] - f[3])
                s23 = dp[ra][rb]
                req = len(s23) + rc + rd
                rem = len(num) - 1 - i
                if req <= rem:
                    suff = '1' * (rem - req) + s23 + '5' * rc + '7' * rd
                    return num[:i] + str(digit) + ''.join(sorted(suff))

        req = len(dp[a][b]) + c + d
        tot = max(len(num) + 1, req)
        ans = '1' * (tot - req) + dp[a][b] + '5' * c + '7' * d
        return ''.join(sorted(ans))
