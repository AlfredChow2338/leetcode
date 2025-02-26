from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum, max_sum, prefix_sum = 0, 0, 0

        for n in nums:
          prefix_sum += n
          min_sum = min(min_sum, prefix_sum)
          max_sum = max(max_sum, prefix_sum)

        return max_sum - min_sum
