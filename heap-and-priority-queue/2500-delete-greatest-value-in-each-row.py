import heapq
from typing import List

# sorting
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        return sum(max(col) for col in zip(*grid))
            
# heap
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        count = 0
        res = 0
        k = len(grid[0])
        while count < k:
            maxV = -1
            for i in range(len(grid)):
                grid[i] = [-abs(c) for c in grid[i]]
                heapq.heapify(grid[i])
                maxV = max(maxV, -heapq.heappop(grid[i]) )
            count += 1
            res += maxV
        return res
            