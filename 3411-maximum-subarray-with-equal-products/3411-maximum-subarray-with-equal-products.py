class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_len, left, prod = 2, 0, 1
        for right, num in enumerate(nums):
            while gcd(prod, num) > 1:
                prod //= nums[left]
                left += 1
            prod *= num
            max_len = max(max_len, right-left+1)
        return max_len