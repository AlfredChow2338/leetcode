from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            curr = nums[i][i]
            res.append("1" if curr == "0" else "0")
        return "".join(res)

# backtracking
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def backtrack(curr):
            if len(curr) == len(nums):
                if curr not in nums:
                    return curr
                return ""
            add_zero = backtrack(curr + "0")
            if add_zero:
                return add_zero
            return backtrack(curr + "1")
        return backtrack("")