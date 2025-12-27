class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        t = meetings[0][0]
        n_ends = [t] * n
        n_counts = [0] * n

        for start, end in meetings:
            n_ends_min = min(n_ends)
            t = n_ends_min if start < n_ends_min else start
            for i in range(len(n_ends)):
                if n_ends[i] <= t:
                    n_ends[i] = t + (end - start)
                    n_counts[i] += 1
                    break

        return n_counts.index(max(n_counts))

