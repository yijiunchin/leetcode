class Solution:
    def validMountainArray(self, arr):
        i, j = 0, len(arr) - 1
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1

        while j > 0 and arr[j - 1] > arr[j]:
            j -= 1

        return 0 < i == j < len(arr) - 1
