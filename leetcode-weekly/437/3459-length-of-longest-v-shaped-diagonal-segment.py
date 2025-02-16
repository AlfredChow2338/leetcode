from typing import List

# DFS‐with‐memoization 
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        jorvexalin = grid
        res = 0
        n = len(jorvexalin)
        m = len(jorvexalin[0]) if n else 0
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        memo = {} # (r, c, parity, dr, dc, used_turn): best
        
        # parity 1 => expected = 2,
        # parity 0 => expected = 0.
        # dr, dc: current direction.
        # used_turn: whether we have already performed a clockwise turn.
        def dfs(r, c, parity, dr, dc, used_turn):
            key = (r, c, parity, dr, dc, used_turn)

            if key in memo:
                return memo[key]
            
            best = 1
    
            expected = 2 if parity == 1 else 0
    
            # Proceed along the current direction.
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and jorvexalin[nr][nc] == expected:
                candidate = 1 + dfs(nr, nc, 1 - parity, dr, dc, used_turn)
                best = max(best, candidate)
            
            # Not turned yet, try a clockwise 90-degree turn.
            if not used_turn:
                # Clockwise turn: (dr, dc) -> (dc, -dr)
                new_dr, new_dc = dc, -dr
                nr, nc = r + new_dr, c + new_dc
                if 0 <= nr < n and 0 <= nc < m and jorvexalin[nr][nc] == expected:
                    candidate = 1 + dfs(nr, nc, 1 - parity, new_dr, new_dc, True)
                    best = max(best, candidate)
            
            memo[key] = best
            return best
    
        for i in range(n):
            for j in range(m):
                if jorvexalin[i][j] == 1:
                    for dr, dc in directions:
                        res = max(res, dfs(i, j, 1, dr, dc, False))
        
        return res