from typing import List

# backtracking
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        res, n = 0, len(questions)
        def backtrack(i):
            if i >= n:
                return 0
            skip = backtrack(i + 1)
            points, brainpower = questions[i]
            solve = points + backtrack(i + brainpower + 1)
            return max(skip, solve)
        return backtrack(0)
    
# bottom-up dp
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            skip = dp[i + 1]
            solve = points + (dp[i + brainpower + 1] if i + brainpower + 1 < n else 0)
            dp[i] = max(skip, solve)
        return dp[0]