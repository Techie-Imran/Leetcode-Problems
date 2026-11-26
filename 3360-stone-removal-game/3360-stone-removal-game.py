class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        cnt = 1
        for i in range(10, -1, -1):
            if n-i >= 0:
                n -= i
                cnt += 1
            else:
                break
        return cnt %2 == 0