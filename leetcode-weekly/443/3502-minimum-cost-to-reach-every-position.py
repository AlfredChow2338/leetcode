from typing import List

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res = [0] * len(cost)
        curr = float("inf")
        for i in range(len(cost)):
            curr = min(curr, cost[i])
            res[i] = curr
        return res