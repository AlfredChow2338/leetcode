from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        res, cost_m = [], {}
        for x, y, _ in edges:
            uf.union(x, y)
        for x, y, weight in edges:
            r = uf.find(x)
            if r not in cost_m:
                cost_m[r] = weight
            else:
                cost_m[r] &= weight
        for x, y in query:
            rx, ry = uf.find(x), uf.find(y)
            if rx != ry:
                res.append(-1)
            else:
                res.append(cost_m[rx])
        return res  
        
        