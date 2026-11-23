class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern) != len(word):
            return False
        ch_word = {}
        word_ch = {}
        for c, w in zip(pattern, word):
            if c not in ch_word:
                if w not in word_ch:
                    ch_word[c] = w
                    word_ch[w] = c
                else:
                    return False
            else:
                if ch_word[c] != w:
                    return False
        return True