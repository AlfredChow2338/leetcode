from collections import defaultdict
from typing import List

# Hash Map
# Time Limit Exceeded
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def checkAnagram (str1: str, str2: str) -> bool:
            if (len(str1) != len(str2)):
                return False

            dict = {}

            for i in range(len(str1)):
                dict[str1[i]] = dict.get(str1[i], 0) + 1
                dict[str2[i]] = dict.get(str2[i], 0) - 1
            
            return all(value == 0 for value in dict.values())

        d = {}
        
        for s in strs:
            isAnagram = False
            for k in d:
                if checkAnagram(s,k):
                    isAnagram = True
                    d[k].append(s)
                    break
            if isAnagram == False:
                d[s] = [s]
        
        return d.values()
            

# Hash Map II
# Runtime: 98 ms, faster than 26.05% of Python3 online submissions for Group Anagrams.
# Memory Usage: 22.3 MB, less than 9.22% of Python3 online submissions for Group Anagrams.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # a-z
            for c in s:
                count[ord(c) - ord('a')] += 1 # Map ASCII index to list
            
            result[tuple(count)].append(s) # Use tuple to indicate unique key
        
        return result.values()
        
            
