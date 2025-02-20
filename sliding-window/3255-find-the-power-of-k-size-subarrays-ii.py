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

# sliding window
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = 1
        l = 0

        for r in range(len(nums)):
            if r > 0 and nums[r-1] + 1 == nums[r]:
                count += 1
            if r - l + 1 > k:
                if nums[l] + 1 == nums[l+1]:
                    count -= 1
                l += 1
            if r - l + 1 == k:
                res.append(nums[r] if count == k else -1)

        return res
