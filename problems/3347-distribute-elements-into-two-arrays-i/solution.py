class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1 = nums[0]
        a2 = nums[1]
        arr1 = [a1]
        arr2 = [a2]
        for n in nums[2:]:
            if a1 > a2:
                a1 = n
                arr1.append(a1)
            else:
                a2 = n
                arr2.append(a2)

        return arr1 + arr2

