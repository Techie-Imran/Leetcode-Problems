class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        cnt, maxcnt = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt > maxcnt:
                maxcnt = cnt
        return maxcnt