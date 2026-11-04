class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxalt = 0
        alt = 0
        for i in gain:
            alt += i
            if alt > maxalt:
                maxalt = alt
        return maxalt