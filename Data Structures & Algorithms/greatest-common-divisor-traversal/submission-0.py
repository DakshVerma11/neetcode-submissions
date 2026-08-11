class dsu:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*n
        self.components=n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu==pv:
            return False
        if self.size[pv]>self.size[pu]:
            pu,pv=pv,pu
        self.components-=1
        self.parent[pv]=pu
        self.size[pu]+=self.size[pv]
        return True

    def isConnected(self):
        return self.components == 1
        
    
    
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = dsu(len(nums))

        factor_index = {}  # f -> index of value with factor f
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i

        return uf.isConnected()
        