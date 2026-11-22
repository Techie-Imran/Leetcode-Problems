class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_cnt = -1
        for i in sentences:
            word_cnt = len(i.split())
            max_cnt = max(max_cnt, word_cnt)
        return max_cnt