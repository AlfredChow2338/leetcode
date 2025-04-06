from typing import List

# backtracking
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        def backtrack(i, prev):
            if i == n:
                return []
            # not take
            res = backtrack(i + 1, prev)
            # take
            if nums[i] % prev == 0:
                tmp = [nums[i]] + backtrack(i + 1, nums[i])
                if len(tmp) > len(res):
                    res = tmp
            return res
        return backtrack(0, 1)