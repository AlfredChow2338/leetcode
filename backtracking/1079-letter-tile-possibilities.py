from typing import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        
        def backtrack():
            res = 0
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    res += 1
                    res += backtrack()
                    count[c] += 1
            return res
            
        return backtrack()
