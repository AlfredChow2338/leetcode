from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # step 1: scan left to right
        # step 2: scan top to bottom
        # step 3: check whether counts from step 1 and 2 > 3
        x = [(r[0], r[2]) for r in rectangles]
        y = [(r[1], r[3]) for r in rectangles]
        x.sort()
        y.sort()
        def count(intervals):
            res, prev = 0, -1
            for start, end in intervals:
                if prev <= start:
                    res += 1
                prev = max(prev, end)
            return res
        return count(x) >= 3 or count(y) >= 3