from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                res += 1
                nums[i+1] = nums[i+1] ^ 1
                nums[i+2] = nums[i+2] ^ 1
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return res