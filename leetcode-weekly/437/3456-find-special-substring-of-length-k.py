class Solution:
  def hasSpecialSubstring(self, s: str, k: int) -> bool:
      for i in range(len(s) - k + 1):
          substring = s[i:i + k]
          if len(set(substring)) == 1:
              char = substring[0]
              if i > 0 and s[i - 1] == char:
                  continue
              if i + k < len(s) and s[i + k] == char:
                  continue
              return True
      return False