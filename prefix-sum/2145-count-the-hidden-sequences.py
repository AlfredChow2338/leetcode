from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr, currLower, currUpper = 0, 0, 0
        for diff in differences:
            curr += diff
            currLower = min(currLower, curr)
            currUpper = max(currUpper, curr)
            if currUpper - currLower > upper - lower:
                return 0
        return (upper - lower) - (currUpper - currLower) + 1
            