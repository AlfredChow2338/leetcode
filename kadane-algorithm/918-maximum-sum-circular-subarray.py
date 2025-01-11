from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(n, curMax + n)
            curMin = min(n, curMin + n)
            total += n
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)
        
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
        

