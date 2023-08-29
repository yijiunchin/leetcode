class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        count = 1
        for item in x_str[:len(x_str)//2]:
            if not item == x_str[-count]:
                return False
            count += 1
        return True
