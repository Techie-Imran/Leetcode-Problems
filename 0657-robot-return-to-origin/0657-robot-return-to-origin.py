class Solution:
    def judgeCircle(self, moves: str) -> bool:
        res = 0
        d = {'U': 1j, 'D': -1j, 'R': 1, 'L': -1}
        for i in moves:
            res += d[i]
        return res == 0