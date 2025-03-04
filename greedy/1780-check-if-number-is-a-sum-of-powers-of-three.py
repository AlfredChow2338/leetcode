from cmath import log

class Solution:
  def checkPowersOfThree(self, n: int) -> bool:
    d = int(log(n, 3))
    for i in range(d, -1, -1):
      if n - 3 ** i >= 0:
        n = n - 3 ** i
    return n == 0

# backtracking
class Solution:
  def checkPowersOfThree(self, n: int) -> bool:
    def backtrack(i, curr):
      if curr == n:
        return True
      if curr > n or 3 ** i > n:
        return False
      if backtrack(i + 1, curr + 3 ** i):
        return True
      return backtrack(i+1, curr)
    return backtrack(0, 0)
  
        