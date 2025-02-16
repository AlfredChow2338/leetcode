from typing import List

# Set
# Runtime: 4255 ms, faster than 22.49% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 31.7 MB, less than 74.51% of Python3 online submissions for Longest Consecutive Sequence.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
                
        return longest