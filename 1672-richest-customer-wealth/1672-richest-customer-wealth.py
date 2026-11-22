class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        for i in accounts:
            richest = max(richest, sum(i))
        return richest