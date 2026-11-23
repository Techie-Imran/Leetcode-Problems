class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    return total
                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum