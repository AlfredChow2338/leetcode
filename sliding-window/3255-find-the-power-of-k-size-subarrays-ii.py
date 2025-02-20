from typing import List

# brute force
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        i = k - 1

        while i < len(nums):
            s = nums[i-k+1:i+1]
            maxValue = 0
            for j in range(len(s)):
                if k == 1:
                    res.append(s[j])
                    break
                first, second = 0, 0
                if j < len(s) - 1:
                    first = s[j]
                    second = s[j+1]
                if first and second and second - first != 1:
                    res.append(-1)
                    break
                maxValue = max(maxValue, first, second)
                if j == len(s) - 1:
                    res.append(maxValue)
            i += 1
        return res
