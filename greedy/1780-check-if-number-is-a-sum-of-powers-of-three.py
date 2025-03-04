from cmath import log

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
      d = int(log(n, 3))
      for i in range(d, -1, -1):
        if n - 3 ** i >= 0:
          n = n - 3 ** i
      return n == 0
