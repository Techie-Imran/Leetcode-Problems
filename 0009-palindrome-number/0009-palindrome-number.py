class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp, res = x, 0
        while x>0:
            res = res*10 + (x%10)
            x //= 10
        if temp == res:
            return True
        else:
            return False