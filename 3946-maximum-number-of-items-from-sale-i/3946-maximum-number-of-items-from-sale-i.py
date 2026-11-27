class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)
        knapsack_items = []
        for i in range(n):
            fact, price = items[i]
            freebies = 0
            for j in range(n):
                if i != j and items[j][0] % fact == 0:
                    freebies += 1
            knapsack_items.append((price, 1+freebies))
        dp = [-1] * (budget+1)
        dp[0] = 0
        for price, val in knapsack_items:
            for c in range(budget, price-1, -1):
                if dp[c-price] != -1:
                    dp[c] = max(dp[c], dp[c-price] + val)
        ans = 0
        for c in range(budget+1):
            if dp[c] != -1:
                extras = (budget-c) // min_price
                ans = max(ans, dp[c] + extras)
        return ans