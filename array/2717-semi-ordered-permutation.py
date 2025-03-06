from typing import List

# Runtime: 51 ms, faster than 99.64% of Python3 online submissions for Semi-Ordered Permutation.
# Memory Usage: 16.7 MB, less than 29.54% of Python3 online submissions for Semi-Ordered Permutation.
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        if nums[0] == 1 and nums[-1] == len(nums):
            return 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                start = i
            if nums[i] == len(nums):
                end = i
        
        if nums[0] == 1:
            return len(nums) - end - 1
        
        if nums[-1] == len(nums):
            return start
        
        if start < end:
            return (len(nums) - end - 1) + start
        else:
            return (len(nums) - end - 1) + start - 1