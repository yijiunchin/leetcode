class Solution:
    def replaceElements(self, arr):
        arr_reverse, arr_max = arr[::-1], -1
        for i in range(len(arr_reverse)):
            arr_reverse[i], arr_max = arr_max, max(arr_max, arr_reverse[i])

        return arr_reverse[::-1]
