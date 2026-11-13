class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if  s == "":
            return True
        sc = tc = 0
        while sc < len(s) and tc < len(t):
            if s[sc] == t[tc]:
                sc += 1
            if sc == len(s):
                return True
            tc += 1
        return False