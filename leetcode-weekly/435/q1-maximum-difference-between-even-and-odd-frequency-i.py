class Solution:
    def maxDifference(self, s: str) -> int:
      m = {}
      maxOdd, minEven = 0, 99999 
      for c in s:
        if c in m:
          m[c] += 1
        else:
          m[c] = 1
      for k in m.keys():
        if m[k] % 2 == 0:
          minEven = min(minEven, m[k])
        else:
          maxOdd = max(maxOdd, m[k])
      return maxOdd - minEven