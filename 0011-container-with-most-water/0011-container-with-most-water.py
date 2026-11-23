class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxw = 0
        left, right = 0, len(height) - 1
        while left < right:
            minw = min(height[left], height[right])
            dist = right - left
            maxw = max(maxw, dist * minw)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxw