class Solution:
    def findValidPair(self, s: str) -> str:
      res = ""
      m = {}
      for c in s:
        if c in m:
          m[c] += 1
        else:
          m[c] = 1
      for i in range(len(s) - 1):
        first_digit = s[i]
        second_digit = s[i + 1]

        if first_digit != second_digit:
          if m[first_digit] == int(first_digit) and m[second_digit] == int(second_digit):
            return first_digit + second_digit

      return ""