from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res, i_max, d_max, n = 0, 0, 0, len(nums)
        for i in range(n):
            res = max(res, (d_max * nums[i]))
            i_max = max(i_max, nums[i])
            d_max = max(d_max, (i_max - nums[i]))
        return res