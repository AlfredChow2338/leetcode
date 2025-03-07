# top-down
class Solution:
  def climbStairs(self, n: int) -> int:
    cache = [-1] * n
    def backtrack(i):
      if i >= n:
        return i == n
      if cache[i] != -1:
        return cache[i]
      cache[i] = backtrack(i+1) + backtrack(i+2) 
      return cache[i]
    
    return backtrack(0)

# bottom-up
class Solution:
  def climbStairs(self, n: int) -> int:
    # 1: 1 (1)
    # 2: 1+1, 2 (2)
    # 3: 1+1+1, 1+2, 2+1 (3)
    # 4: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 (5)
    # 5: 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1 (8)
    if n <= 2:
      return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 2, 3
    for i in range(3, n + 1):
      dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# bottom-up II
class Solution:
  def climbStairs(self, n: int) -> int:
    one, two = 1, 1

    for i in range(n - 1):
      one, two = one + two, one
    
    return one

    