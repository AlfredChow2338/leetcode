class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        L, R = 0, 1
        res = []
        while R < len(nums):
          if nums[L] == nums[R]:
            nums[L] *= 2
            nums[R] = 0
            L = R + 1
            R = L + 1
            continue
          L += 1
          R += 1
        
        for n in nums:
          if n != 0:
            res.append(n)
        
        while len(res) < len(nums):
          res.append(0)
        
        return res
