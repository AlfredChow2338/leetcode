from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, max(candies)
        def checkPossible(n):
            if n == 0:
                return False
            maxNum = 0
            for c in candies:
                maxNum += c // n
                if maxNum >= k:
                    return True
            return False
        while left < right:
            mid = (left + right + 1) // 2
            if checkPossible(mid):
                left = mid
            else:
                right = mid - 1
        return left