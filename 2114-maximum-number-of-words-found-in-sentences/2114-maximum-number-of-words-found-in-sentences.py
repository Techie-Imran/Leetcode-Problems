class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_cnt = -1
        for i in range(len(sentences)):
            word_cnt = len(sentences[i].split())
            max_cnt = max(max_cnt, word_cnt)
        return max_cnt