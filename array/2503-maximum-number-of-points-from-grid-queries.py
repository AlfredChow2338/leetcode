from collections import deque
from heapq import heappop, heappush
from typing import List

# brute force
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        res = [0] * len(queries)
        ROW, COL = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # right, left, up, down
        for i, v in enumerate(queries):
            q = deque([(0, 0)])
            visit = [[0] * COL for _ in range(ROW)]
            visit[0][0] = 1
            points = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] >= v:
                        continue
                    points += 1
                    for r1, c1 in directions:
                        r2 = r + r1
                        c2 = c + c1
                        if (
                            0 <= r2 < ROW
                            and (0 <= c2 < COL)
                            and not visit[r2][c2]
                            and grid[r2][c2] < v
                        ):
                            q.append((r2, c2))
                            visit[r2][c2] = 1
                res[i] = points
        return res

# heap
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROW, COL = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # right, left, down, up
        sorted_queries = sorted([(v, i) for i, v in enumerate(queries)])
        res = [0] * len(queries)
        heap = [(grid[0][0], 0, 0)]  # (value, row, col)
        visited = [[False] * COL for _ in range(ROW)]
        visited[0][0] = True
        points, cv = 0, 0
        for v, i in sorted_queries:
            while heap and heap[0][0] < v:
                val, r, c = heappop(heap)
                if val != cv:
                    cv = val
                points += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROW and 0 <= nc < COL and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heappush(heap, (grid[nr][nc], nr, nc))
            res[i] = points
        return res