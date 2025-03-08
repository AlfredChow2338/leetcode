class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res, numW = 0, 0
        n = len(blocks)
        if n < k:
            return res
        for i in range(k):
            if blocks[i] == "W":
                res += 1
                numW += 1
        j = 0
        for i in range(k, n):
            if blocks[i] == "W":
                numW += 1
            if blocks[j] == "W":
                numW -= 1
            j += 1
            res = min(res, numW)
        return res
