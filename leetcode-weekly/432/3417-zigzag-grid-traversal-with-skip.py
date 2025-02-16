from typing import List

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
      res = []
      for i in range(len(grid)):
        row = grid[i]
        if i % 2 == 0:
          for j in range(len(row)):
            if j % 2 == 0:
              res.append(row[j])
        else:
          for j in range(len(row) - 1, 0, -1):
            if j % 2 != 0:
              res.append(row[j])
      return res
            