import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)

        while True:
            v = heapq.heappop(h)
            k -= 1
            if k == 0:
                return -v