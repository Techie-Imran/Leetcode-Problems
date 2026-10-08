class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second = -1
        for ch in s:
            if ch.isdigit():
                c = int(ch)
                if(c > largest):
                    second = largest
                    largest = c
                if(c < largest and c > second):
                    second = c
        return second