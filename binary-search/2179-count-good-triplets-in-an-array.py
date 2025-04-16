from bisect import bisect_left
from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res, n, q = 0, len(nums1), []
        i_map = {x: i for i,x in enumerate(nums2)} # num2 -> index
        for i, num1 in enumerate(nums1):
            index = bisect_left(q, i_map[num1])
            q.insert(index, i_map[num1])
            res += index * (n - 1 - i_map[num1] - i + index)
        return res