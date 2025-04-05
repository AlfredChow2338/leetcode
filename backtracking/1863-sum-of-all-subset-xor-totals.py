from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # XOR ^
        # 5, 1, 6 = (5), (1), (6), (5, 1), (5, 6), (1, 6), (5, 1, 6)
        n = len(nums)
        def backtrack(i, curr):
            if i == n:
                return curr
            take = backtrack(i + 1, curr ^ nums[i])
            not_take = backtrack(i + 1, curr)
            return take + not_take
        return backtrack(0, 0)
                