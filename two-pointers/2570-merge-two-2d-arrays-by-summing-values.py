from typing import List

# hash map
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = {}
        res = []
        for n in nums1:
          id, v = n
          m[id] = v
        
        for n in nums2:
          id, v = n
          m[id] = v + m.get(id, 0)
        
        for k in m:
          res.append([k, m[k]])
        
        return sorted(res, key=lambda x: x[0])
        
# two pointer
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        res = []

        while p1 < n1 and p2 < n2:
          if nums1[p1][0] == nums2[p2][0]:
            res.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
            p1 += 1
            p2 += 1
            continue
          if nums1[p1][0] < nums2[p2][0]:
            res.append(nums1[p1])
            p1 += 1
            continue
          res.append(nums2[p2])
          p2 += 1

        while p1 < n1:
          res.append(nums1[p1])
          p1 += 1

        while p2 < n2:
          res.append(nums2[p2])
          p2 += 1
        
        return res

        

          

          