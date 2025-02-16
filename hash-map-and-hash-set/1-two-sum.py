from typing import List

# Two Pointers
# Output Limit Exceeded
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        left = 0
        right = 0
        while left < len(nums):
            right += 1
            
            if nums[left] + nums[right] == target:
                return [left, right]
            
            if right == len(nums) - 1:
                left += 1
                right = left
              
# Hash Map
# Runtime: 55 ms, faster than 81.36% of Python3 online submissions for Two Sum.
# Memory Usage: 18.1 MB, less than 7.76% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            if n in dict:
                return [dict[n], i]
            dict[target - n] = i


        