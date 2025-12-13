class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        electronics, grocery, pharmacy, restaurant = [], [], [], []

        for i in range(len(code)):
            if not code[i]:
                continue

            if isActive[i] is not True:
                continue

            if not all(c.isalnum() or c == '_' for c in code[i]):
                continue

            if businessLine[i].startswith('e'): electronics.append(code[i])
            elif businessLine[i].startswith('g'): grocery.append(code[i])
            elif businessLine[i].startswith('p'): pharmacy.append(code[i])
            elif businessLine[i].startswith('r'): restaurant.append(code[i])

        return sorted(electronics) + sorted(grocery) + sorted(pharmacy) + sorted(restaurant)

