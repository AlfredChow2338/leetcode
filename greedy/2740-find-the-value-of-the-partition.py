from typing import List

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        res = float("inf")
        for x, y in zip(nums, nums[1:]):
            res = min(res, y - x)
        return res
