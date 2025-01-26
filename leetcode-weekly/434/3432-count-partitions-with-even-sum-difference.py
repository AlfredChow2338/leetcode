from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
      L = 0
      count = 0
      while L < len(nums) - 1:
        lsum = sum(nums[0:L+1])
        rsum = sum(nums[L+1:])
        L += 1
        if (lsum - rsum) % 2 == 0:
          count += 1
      return count
        