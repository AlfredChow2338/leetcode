from typing import List

# brute force
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res = [True for _ in range(days)]
        for start, end in meetings:
            for i in range(start, end+1):
                res[i-1] = False
        return sum(r for r in res)
    
# sorting
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # step 1: sort meetings
        # step 2: increment gap between 2 meetings
        # step 3: increment gap after the last meeting
        res, prevEnd = 0, 0
        meetings.sort()
        for start, end in meetings:
            if start > prevEnd + 1: 
                res += start - prevEnd - 1
            prevEnd = max(prevEnd, end)
        res += days - prevEnd
        return res
