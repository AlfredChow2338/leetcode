import collections
from typing import List

# Hash Map
# Runtime: 96 ms, faster than 34.03% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 16.5 MB, less than 82.59% of Python3 online submissions for Valid Sudoku.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        cols = collections.defaultdict(set) 
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)
        
        for r in range(n):
            for c in range(n):
                v = board[r][c]
                if v == '.':
                    continue
                if (v in rows[r] or v in cols[c] or v in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(v)
                rows[r].add(v)
                squares[(r // 3, c // 3)].add(v)
        
        return True
        