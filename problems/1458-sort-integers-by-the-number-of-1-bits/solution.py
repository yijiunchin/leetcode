class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        groups = {}
        for n in arr:
            count = bin(n)[2:].count('1')
            if groups.get(count) == None:
                groups[count] = [n]
            else:
                groups[count].append(n)

        ans = []
        groups = dict(sorted(groups.items()))
        print(groups)
        for v in groups.values():
            ans.extend(sorted(v))

        return ans
