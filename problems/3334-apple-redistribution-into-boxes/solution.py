class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        for i, c in enumerate(capacity, 1):
            total -= c
            if total <= 0:
                return i
        return len(capacity)

