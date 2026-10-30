class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        res = [0]*n
        i, j = 0, 1
        while(i < n or j < n):
            res[i] = nums[j]
            res[j] = nums[i]
            i += 2
            j += 2
        return res