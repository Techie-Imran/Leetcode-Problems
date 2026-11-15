class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        tot = 0
        min_size = float('inf')
        for right in range(len(nums)):
            tot += nums[right]
            
            while tot >= target:
                min_size = min(min_size, right - left + 1)
                tot -= nums[left]
                left += 1
        return min_size if min_size != float('inf') else 0