from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
      res = [0] * 2
      l = [0] * len(grid)**2
      
      for i in range(len(grid)):
        for j in range(len(grid)):
          l[grid[i][j] - 1] = 1 + l[grid[i][j] - 1]
      
      for i in range(len(l)):
        if l[i] == 2:
          res[0] = i + 1
        if l[i] == 0:
          res[1] = i + 1

      return res
