from typing import List

# list
# Runtime: 79 ms, faster than 37.30% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 18 MB, less than 45.99% of Python3 online submissions for Remove Duplicates from Sorted Array.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        ns = []
        for n in nums:
            if n not in ns:
                nums[l] = n
                ns.append(n)
                l += 1
        return len(ns)


# Two Pointers
# Runtime: 78 ms, faster than 42.15% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 18 MB, less than 8.85% of Python3 online submissions for Remove Duplicates from Sorted Array.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      j = 1
      for i in range(1, len(nums)):
          if nums[i] != nums[i - 1]:
              nums[j] = nums[i]
              j += 1
      return j