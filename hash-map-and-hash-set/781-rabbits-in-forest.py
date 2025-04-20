from math import ceil
from typing import Counter, List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        res = 0
        for n in c:
            res += ceil(c[n] / (n + 1)) * (n + 1)
        return res