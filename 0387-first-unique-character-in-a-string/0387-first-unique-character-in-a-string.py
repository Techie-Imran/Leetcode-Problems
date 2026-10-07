class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = {}
        for c in s:
            arr[c] = arr.get(c,0)+1
        for i, c in enumerate(s):
            if arr[c] == 1:
                return i
        return -1
