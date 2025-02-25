from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0

        while r < len(nums):
            while r + 1 < len(nums) and nums[r] == 0:
                r += 1
            if nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1

        