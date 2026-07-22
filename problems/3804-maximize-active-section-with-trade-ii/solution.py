class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        zeros = [(m.start(), m.end() - 1) for m in re.finditer(r'0+', s)]
        total_1s = s.count('1')
        if len(zeros) < 2:
            return [total_1s] * len(queries)

        u = [z[0] for z in zeros]
        v = [z[1] for z in zeros]
        L0 = [z[1] - z[0] + 1 for z in zeros]
        L1 = [u[i + 1] - v[i] - 1 for i in range(len(zeros) - 1)]
        S0 = [L0[i] + L0[i + 1] for i in range(len(zeros) - 1)]

        def build_st_max(arr):
            st = [arr]
            for i in range(1, len(arr).bit_length()):
                st.append([max(st[-1][j], st[-1][j + (1 << (i - 1))]) for j in range(len(arr) - (1 << i) + 1)])
            return st

        def build_st_min(arr):
            st = [arr]
            for i in range(1, len(arr).bit_length()):
                st.append([min(st[-1][j], st[-1][j + (1 << (i - 1))]) for j in range(len(arr) - (1 << i) + 1)])
            return st

        def query_st_max(st, l, r):
            if l > r:
                return 0
            i = (r - l + 1).bit_length() - 1
            return max(st[i][l], st[i][r - (1 << i) + 1])

        def query_st_min(st, l, r):
            if l > r:
                return float('inf')
            i = (r - l + 1).bit_length() - 1
            return min(st[i][l], st[i][r - (1 << i) + 1])

        st_L0_max = build_st_max(L0)
        st_L1_min = build_st_min(L1)
        st_S0_max = build_st_max(S0)

        ans = []
        for l, r in queries:
            p = bisect.bisect_left(v, l)
            q = bisect.bisect_right(u, r) - 1
            if p >= q:
                ans.append(total_1s)
                continue

            z1 = min(r, v[p]) - max(l, u[p]) + 1
            zk = min(r, v[q]) - max(l, u[q]) + 1

            m_val = max(z1, zk, query_st_max(st_L0_max, p + 1, q - 1))
            min_o = query_st_min(st_L1_min, p, q - 1)

            if q - p == 1:
                max_adj = z1 + zk
            else:
                max_adj = max(z1 + L0[p + 1], zk + L0[q - 1], query_st_max(st_S0_max, p + 1, q - 2))

            ans.append(total_1s + max(max_adj, m_val - min_o))

        return ans
