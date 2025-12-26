class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers_len = len(customers)
        ps = [0] * (customers_len + 1)
        for i in range(customers_len):
            if customers[i] == 'Y': ps[i + 1] = ps[i] + 1
            else: ps[i + 1] = ps[i] - 1
        return ps.index(max(ps))
