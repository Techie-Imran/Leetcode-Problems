class Solution:
    def canAliceWin(self, n: int) -> bool:
        cnt = 0
        tot = 10
        while n >= tot > 0:
            n -= tot
            tot -= 1
            cnt += 1
        return cnt %2 == 1