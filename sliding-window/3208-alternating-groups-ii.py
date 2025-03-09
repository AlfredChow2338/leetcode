from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res, count, left = 0, 0, 0
        n = len(colors)
        if k > n:
            return res
        for i in range(k - 1):
            colors.append(colors[i])
        for right in range(n + k - 2):
            if colors[right] != colors[right + 1]:
                count += 1
            else:
                count = 0
            if count == k - 1:
                res += 1
                count -= 1
        return res
