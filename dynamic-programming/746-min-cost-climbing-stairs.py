from typing import List

# top-down
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      memo = [-1] * len(cost)
      def backtrack(i):
        if i >= len(cost):
          return 0
        if memo[i] != -1:
          return memo[i]
        memo[i] = cost[i] + min(backtrack(i+1), backtrack(i+2))
        return memo[i]
      
      return min(backtrack(0), backtrack(1))