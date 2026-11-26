class Solution:
    def canAliceWin(self, n: int) -> bool:
        cnt, tot = 0, 10
        while n >= tot > 0:
            n -= tot
            tot -= 1
            cnt += 1
        return cnt %2 == 1