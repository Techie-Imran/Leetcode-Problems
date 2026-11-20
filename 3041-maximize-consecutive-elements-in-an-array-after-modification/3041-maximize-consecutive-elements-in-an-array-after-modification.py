class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        max_len = 0
        for i in nums:
            dp[i + 1] = dp[i] + 1
            dp[i] = dp[i - 1] + 1
            max_len = max(max_len, dp[i + 1], dp[i])
        return max_len