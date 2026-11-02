class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n > 0:
            j = 0
        else:
            return nums1
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1
        nums1.sort()
        return nums1
            