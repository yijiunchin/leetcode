class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        skip = 0
        for i in range(len(arr)):
            if skip > 0:
                skip -= 1
                continue

            if arr[i] == 0:
                arr.insert(i + 1, 0)
                del arr[-1]
                skip += 1
