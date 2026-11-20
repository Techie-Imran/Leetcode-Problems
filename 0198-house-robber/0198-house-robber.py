class Solution:
    def rob(self, nums: list[int]) -> int:
        prev1 = 0
        prev2 = 0
        for i in nums:
            curr = max(i + prev2, prev1)
            prev2, prev1 = prev1, curr
        return curr