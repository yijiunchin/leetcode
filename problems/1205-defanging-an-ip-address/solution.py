class Solution:
    def defangIPaddr(self, address: str) -> str:
        addresses = address.split('.')

        ans = ''
        
        for a in range(len(addresses)):
            ans += addresses[a]
            if a != len(addresses) - 1:
                ans += '[.]'
        return ans
