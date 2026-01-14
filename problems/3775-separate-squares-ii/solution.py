class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        events = []
        xs = set()
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs.add(x)
            xs.add(x + l)

        events.sort()
        sorted_xs = sorted(list(xs))
        x_map = {x: i for i, x in enumerate(sorted_xs)}
        num_x = len(sorted_xs)

        count = [0] * (4 * num_x)
        length = [0.0] * (4 * num_x)

        def update(node, start, end, l, r, val):
            if l <= start and end <= r:
                count[node] += val
            else:
                mid = (start + end) // 2
                if l < mid:
                    update(2 * node, start, mid, l, r, val)
                if r > mid:
                    update(2 * node + 1, mid, end, l, r, val)

            if count[node] > 0:
                length[node] = sorted_xs[end] - sorted_xs[start]
            else:
                if end - start > 1:
                    length[node] = length[2 * node] + length[2 * node + 1]
                else:
                    length[node] = 0

        areas = []
        total_area = 0.0
        for i in range(len(events) - 1):
            y, type, x1, x2 = events[i]
            update(1, 0, num_x - 1, x_map[x1], x_map[x2], type)
            h = events[i+1][0] - y
            if h > 0:
                step_area = length[1] * h
                areas.append((y, events[i+1][0], length[1]))
                total_area += step_area

        target = total_area / 2.0
        current_area = 0.0
        for y_start, y_end, l in areas:
            step = l * (y_end - y_start)
            if current_area + step >= target - 1e-9:
                return y_start + (target - current_area) / l
            current_area += step

        return float(events[-1][0])

