from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        leftCount, n = 0, len(nums)
        counter = Counter(nums)
        maxKey = max(counter, key=counter.get)
        maxCount = counter[maxKey]
        for i in range(n - 1):
            if nums[i] == maxKey:
                leftCount += 1
            if leftCount > (i + 1) / 2 and (maxCount - leftCount) > (n - i - 1) / 2:
                return i
        return -1