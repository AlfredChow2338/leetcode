from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # goal: max(cost of subarrays) - min(cost of subarrays)
        n = len(weights)
        if k == 1:
            return 0
        diff = [weights[i + 1] + weights[i] for i in range(n - 1)]
        diff.sort() # diff: [4, 6, 8] given weight: [1,3,5,1], k: 2
        return sum(diff[-(k-1):]) - sum(diff[:k-1])