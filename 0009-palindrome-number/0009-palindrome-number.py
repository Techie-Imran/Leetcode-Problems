class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp, res = x, 0
        if x<0:
            return False
        while x>0:
            res = res*10 + (x%10)
            x //= 10
        return temp == res