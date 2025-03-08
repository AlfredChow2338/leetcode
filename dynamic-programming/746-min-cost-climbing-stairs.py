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

# bottom-up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      dp = [0] * (len(cost) + 1)

      for i in range(2, len(cost) + 1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
      
      return dp[len(cost)]
        