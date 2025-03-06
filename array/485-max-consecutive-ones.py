from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        
        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
                res = max(res, count)
        return res
            