class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern) != len(word):
            return False
        seen_p = {}
        seen_w = {}
        for char, word in zip(pattern, word):
            if char in seen_p and seen_p[char] != word:
                return False
            if word in seen_w and seen_w[word] != char:
                return False
            seen_p[char] = word
            seen_w[word] = char
        return True