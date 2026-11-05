class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        cnt = 0
        j = len(arr1) - 1
        while j >= 0:
            res = True
            for i in range(len(arr2)):
                if(abs(arr1[j]-arr2[i]) <= d):
                    res = False
            if res:
                cnt += 1
            j -= 1
        return cnt