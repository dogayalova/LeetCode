from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_alice = UnionFind(n + 1)
        uf_bob = UnionFind(n + 1)
        
        used_edges = 0
        
        # Process type 3 edges first
        for type, u, v in edges:
            if type == 3:
                if uf_alice.union(u, v):
                    uf_bob.union(u, v)
                    used_edges += 1
        
        # Process type 1 and type 2 edges
        for type, u, v in edges:
            if type == 1:
                if uf_alice.union(u, v):
                    used_edges += 1
            elif type == 2:
                if uf_bob.union(u, v):
                    used_edges += 1
        
        # Check if both graphs are fully traversable
        if all(uf_alice.find(i) == uf_alice.find(1) for i in range(1, n + 1)) and \
           all(uf_bob.find(i) == uf_bob.find(1) for i in range(1, n + 1)):
            return len(edges) - used_edges
        else:
            return -1

