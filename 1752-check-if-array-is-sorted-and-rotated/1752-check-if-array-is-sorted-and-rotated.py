class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        cnt = 1
        for i in range(1, n * 2):
            if nums[(i-1)%n] <= nums[i%n]:
                cnt += 1
            else:
                cnt = 1
            if cnt == n:
                return True
        return n==1