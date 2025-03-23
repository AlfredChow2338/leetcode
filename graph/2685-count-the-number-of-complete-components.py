from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # goal: count complete (inter-connected) component: graph (dfs, bfs)
        # step 1: construct adjacency map
        # step 2: construct component (dfs)
        # step 3: for n-node graph, each node should have (n-1) edges to be complete
        res = 0
        adj, visited = defaultdict(list), set()
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        def dfs(node, comp):
            if node in visited:
                return
            visited.add(node)
            comp.append(node)
            for nei in adj[node]:
                dfs(nei, comp)
            return comp
        for i in range(n):
            if i in visited:
                continue
            component = dfs(i, []) # construct component
            # check if all nodes in the component has n-1 edges
            if all([len(component) - 1 == len(adj[v]) for v in component]):
                res += 1
        return res


