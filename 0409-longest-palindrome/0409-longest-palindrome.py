class Solution:
    def longestPalindrome(self, s: str) -> int:
        pair = set()
        length = 0
        for char in s:
            if char in pair:
                length += 2
                pair.remove(char)
            else:
                pair.add(char)
        if pair:
            length += 1
        return length