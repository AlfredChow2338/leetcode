from typing import List

# Hashset
# Runtime: 463 ms, faster than 48.30% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 29.8 MB, less than 68.58% of Python3 online submissions for Contains Duplicate II.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs = {}
        
        for idx in range(len(nums)):
            if nums[idx] in hs and abs(idx - hs[nums[idx]]) <= k:
                return True
            hs[nums[idx]] = idx
        return False

# Sliding window
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                w.remove(nums[L])
                L += 1
            if nums[R] in w:
                return True
            w.add(nums[R])

        return False