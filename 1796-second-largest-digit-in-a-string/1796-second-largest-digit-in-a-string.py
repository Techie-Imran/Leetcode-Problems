class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second = -1
        digits = []
        for ch in s:
            if ch.isdigit():
                if ch not in digits:
                    digits.append(ch)
        digits.sort(reverse=True)
        if len(digits) < 2:
            return -1
        return int(digits[1])