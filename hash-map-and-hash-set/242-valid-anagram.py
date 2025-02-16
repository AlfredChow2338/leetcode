from typing import Counter

# Dictionary I
# Runtime: 56 ms, faster than 22.71% of Python3 online submissions for Valid Anagram.
# Memory Usage: 16.8 MB, less than 84.16% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for c in range(len(s)):
            if s[c] in dict:
                dict[s[c]] += 1
            else:
                dict[s[c]] = 1
        for c in range(len(t)):
            if t[c] in dict:
                dict[t[c]] -= 1
            else:
                dict[t[c]] = -1
        for k in dict:
            if dict[k] != 0:
                return False
        return True
    
# Counter
# Runtime: 51 ms, faster than 47.41% of Python3 online submissions for Valid Anagram.
# Memory Usage: 17 MB, less than 44.60% of Python3 online submissions for Valid Anagram.
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
      return Counter(s) == Counter(t)
  
# Sort
# Runtime: 63 ms, faster than 6.74% of Python3 online submissions for Valid Anagram.
# Memory Usage: 17.2 MB, less than 25.57% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
# Dictionary II
# Runtime: 53 ms, faster than 36.14% of Python3 online submissions for Valid Anagram.
# Memory Usage: 16.9 MB, less than 84.16% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for c in range(len(s)):
            dict[s[c]] = dict.get(s[c], 0) + 1
        for c in range(len(t)):
            dict[t[c]] = dict.get(t[c], 0) - 1
        for k in dict:
            if dict[k] != 0:
                return False
        return True