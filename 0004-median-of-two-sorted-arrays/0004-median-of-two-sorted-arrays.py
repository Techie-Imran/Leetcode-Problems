class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merge_list = sorted(nums1 + nums2)
        n = len(merge_list)
        if n%2 == 1:
            return float(merge_list[n//2])
        else:
            return float(merge_list[n//2] + merge_list[n//2 - 1]) / 2.0