class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        while stack:
            i = stack.pop()
            if 0 <= i < len(arr) and arr[i] >= 0:
                if arr[i] == 0:
                    return True
                stack.extend([i + arr[i], i - arr[i]])
                arr[i] = -1
        return False
