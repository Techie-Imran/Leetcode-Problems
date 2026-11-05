class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        freq = {}
        res = [0]*2
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        for i, j in freq.items():
            res[0] += j//2
            res[1] += j%2
        return res
