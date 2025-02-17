from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        res = [[0 for _ in range(C)] for _ in range(R)]

        for r in range(R):
            for c in range(C):
                tl, br = set(), set()
                nr, nc = r - 1, c - 1
                while 0 <= nr < R and 0 <= nc < C:
                    tl.add(grid[nr][nc])
                    nr -= 1
                    nc -= 1
                nr, nc = r + 1, c + 1
                while 0 <= nr < R and 0 <= nc < C:
                    br.add(grid[nr][nc])
                    nr += 1
                    nc += 1
                res[r][c] = abs(len(tl) - len(br))

        return res