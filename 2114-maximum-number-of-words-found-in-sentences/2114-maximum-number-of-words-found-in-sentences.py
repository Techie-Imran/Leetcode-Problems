class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_cnt = -1
        for s in sentences:
            word_cnt = len(s.split())
            max_cnt = max(max_cnt, word_cnt)
        return max_cnt