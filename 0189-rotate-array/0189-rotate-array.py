class Solution:
    def circle(self, arr: list[int], l: int, r: int) -> None:
        while(l < r):
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        if n < 2 or k == 0:
            return
        self.circle(nums, 0, n-k-1)
        self.circle(nums, n-k, n-1)
        self.circle(nums, 0, n-1)