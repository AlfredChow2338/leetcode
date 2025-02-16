from typing import List

# Dictionary
# Runtime: 426 ms, faster than 32.15% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 34.6 MB, less than 14.97% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = 1
        return False
        
# Sort and Two Pointer
# Runtime: 458 ms, faster than 9.97% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 28.2 MB, less than 95.89% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left = 0
        right = 1
        while right < len(nums):
            if (nums[left] == nums[right]):
                return True
            left += 1
            right += 1
        return False

# Hash Set
# Runtime: 410 ms, faster than 80.61% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 32 MB, less than 45.93% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False