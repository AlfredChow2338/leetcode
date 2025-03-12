from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        res, zero, n = 0, 0, len(nums)
        for num in nums:
            if num == 0:
                zero += 1
                continue
            if num > 0:
                break
            res += 1
        if res >= n - zero - res:
            return res
        return n - zero - res