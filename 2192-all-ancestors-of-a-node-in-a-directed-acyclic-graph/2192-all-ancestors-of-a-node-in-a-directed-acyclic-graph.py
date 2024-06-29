from collections import deque, defaultdict
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: Create the adjacency list and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Step 2: Perform topological sort using Kahn's algorithm
        topo_sort = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Initialize ancestor sets
        ancestors = [set() for _ in range(n)]
        
        # Step 4: Propagate ancestors using topological order
        for node in topo_sort:
            for neighbor in graph[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
        
        # Step 5: Convert sets to sorted lists
        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        
        return result