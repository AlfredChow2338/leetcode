from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            curr = nums[i][i]
            res.append("1" if curr == "0" else "0")
        return "".join(res)