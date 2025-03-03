from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = []
        for n in nums:
            if n < pivot:
                res.append(n)
        
        for n in nums:
            if n == pivot:
                res.append(n)
        
        for n in nums:
            if n > pivot:
                res.append(n)

        return res

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        L, R = 0, len(nums) - 1
        res = [0] * len(nums)

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                res[L] = nums[i]
                L += 1
            if nums[j] > pivot:
                res[R] = nums[j]
                R -= 1

        while L <= R:
            res[L] = pivot
            L += 1

        return res