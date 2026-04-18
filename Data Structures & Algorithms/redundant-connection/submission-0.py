class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

    def connected(self, i, j):
        """Checks if i and j are in the same set."""
        return self.find(i) == self.find(j)
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf=UnionFind(1000)
        for i,j in edges:
            if uf.connected(i,j):
                return [i,j]
            uf.union(i,j)