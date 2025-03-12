from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        res, zero, n = 0, 0, len(nums)
        for num in nums:
            if num == 0:
                zero += 1
                continue
            if num > 0:
                break
            res += 1
        if res >= n - zero - res:
            return res
        return n - zero - res
    
# binary search
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        smallerZero, biggerZero = n, n
        
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1 
                smallerZero = mid
        
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1
                biggerZero = mid
        
        return max(n - biggerZero, smallerZero)

        