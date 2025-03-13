from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        res = 0
        for q in queries:
            l, r, v = q
            if sum(nums) > 0:
                res += 1
            for i in range(l, r+1):
                nums[i] = nums[i] - v if nums[i] - v >= 0 else 0
            if sum(nums) == 0:
                return res
        return -1
    
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        left, right = 0, len(queries)
        def checkRangeOverQueries(k):
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                diff[r+1] -= v
            currSum = 0
            for i in range(n):
                currSum += diff[i]
                if currSum < nums[i]:
                    return False
            return True
        if not checkRangeOverQueries(right):
            return -1
        while left <= right:
            mid = (left + right) // 2
            if checkRangeOverQueries(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left        