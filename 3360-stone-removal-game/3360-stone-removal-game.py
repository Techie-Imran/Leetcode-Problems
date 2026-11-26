class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        cnt = 1
        tot = 10
        while tot > 0 and n-tot >= 0:
            n -= tot
            tot -= 1
            cnt += 1
        return cnt %2 == 0