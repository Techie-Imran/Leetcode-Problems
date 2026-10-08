class Solution:
    def cycle(self, arr: list[int], l: int, r: int) -> None:
        while(l < r):
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        if n < 2 or k == 0:
            return
        self.cycle(nums, 0, n-1) #[7,6,5,4,3,2,1]
        self.cycle(nums, 0, k-1) #[5,6,7,4,3,2,1]
        self.cycle(nums, k, n-1) #[5,6,7,1,2,3,4]