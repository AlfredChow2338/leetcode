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

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
      N, M = len(str1), len(str2)
      prev = [str2[j:] for j in range(M)]
      prev.append("")

      for i in reversed(range(N)):
        curr = [""] * M
        curr.append(str1[i:])
        
        for j in reversed(range(M)):
          if str1[i] == str2[j]:
            curr[j] = str1[i] + prev[j+1]
          else:
            res1 = str1[i] + prev[j]
            res2 = str2[j] + curr[j+1]
            if len(res1) < len(res2):
              curr[j] = res1
            else:
              curr[j] = res2

        prev = curr
      
      return curr[0]
