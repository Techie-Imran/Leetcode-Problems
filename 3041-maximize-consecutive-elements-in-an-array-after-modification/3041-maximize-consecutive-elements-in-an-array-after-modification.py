class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        for i in nums:
            dp[i + 1] = dp[i] + 1
            dp[i] = dp[i - 1] + 1
        return max(dp.values())