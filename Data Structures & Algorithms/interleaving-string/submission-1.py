class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)
        if n + m != k:
            return False
        dp = {}
        
        def dfs(i, j) -> bool:
            if (i, j) in dp:
                return dp[(i, j)]
                
            if i == n and j == m:
                dp[(i, j)] = True
                return True
            elif i == n:
                dp[(i, j)] = (s2[j:] == s3[i+j:])
                return dp[(i, j)]
            elif j == m:
                dp[(i, j)] = (s1[i:] == s3[i+j:])
                return dp[(i, j)]
            
            # Try matching from s1
            if s1[i] == s3[i+j] and dfs(i+1, j):
                dp[(i, j)] = True
                return True
            # Try matching from s2
            if s2[j] == s3[i+j] and dfs(i, j+1):
                dp[(i, j)] = True
                return True
            
            dp[(i, j)] = False
            return False
        
        return dfs(0, 0)