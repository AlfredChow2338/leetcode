# backtracking, time limit exceeded
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def backtrack(i, j):
          if i == len(str1):
            return str2[j:]

          if j == len(str2):
            return str1[i:]
          
          if str1[i] == str2[j]:
            return str1[i] + backtrack(i+1, j+1)

          res1 = str1[i] + backtrack(i + 1, j)
          res2 = str2[j] + backtrack(i, j + 1)

          return res1 if len(res1) < len(res2) else res2

        return backtrack(0, 0)