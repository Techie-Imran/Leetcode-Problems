class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern) != len(word):
            return False
        seen_p = {}
        seen_w = {}
        for char, word in zip(pattern, word):
            if char not in seen_p:
                if word not in seen_w:
                    seen_p[char] = word
                    seen_w[word] = char
                else:
                    return False
            else:
                if seen_p[char] != word:
                    return False
        return True