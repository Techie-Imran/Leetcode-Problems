class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low, best = prices[0], 0
        for p in prices:
            best = max(best, p-low)
            low = min(low, p)
        return best