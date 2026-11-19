class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        rem_index = {0: -1}
        run_sum = 0
        for i, n in enumerate(nums):
            run_sum += n
            rem = run_sum % k
            if rem in rem_index:
                if i - rem_index[rem] >= 2:
                    return True
            else:
                rem_index[rem] = i
        return False