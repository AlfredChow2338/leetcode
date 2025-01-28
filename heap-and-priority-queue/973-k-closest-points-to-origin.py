import heapq
from typing import List

# Sorting
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2 + point[1]**2
    
        points.sort(key=distance)
        
        return points[:k]

# Min heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap, res = [], []
        for x, y in points:
            dist = x**2 + y**2
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res
