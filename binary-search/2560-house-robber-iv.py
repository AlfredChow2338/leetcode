from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            i, curr = 0, 0
            while i < len(nums):
                if nums[i] <= mid:
                    curr += 1
                    i += 2
                else:
                    i += 1
            if curr >= k:
                right = mid
            else:
                left = mid + 1
        return left