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