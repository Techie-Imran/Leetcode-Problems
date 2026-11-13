class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        tot_pass = time // (n-1)
        rem_pass = time % (n-1)
        if tot_pass%2 == 0:
            return rem_pass + 1
        else:
            return n - rem_pass