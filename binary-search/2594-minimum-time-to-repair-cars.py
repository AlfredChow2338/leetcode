from cmath import sqrt
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        res = 0
        l, r = 1, ranks[0] * cars * cars # use any of rank for max
        def isEnough(t):
            count = 0
            for r in ranks:
                # t = r * n^2
                # n = sqrt(t / r)
                count += int(sqrt(t / r))
            return count >= cars
        while l <= r:
            mid = (l + r) // 2
            if isEnough(mid):
                res = mid
                r = mid - 1 # enough -> try smaller value
            else:
                l = mid + 1 # not enough -> try bigger value
        return l