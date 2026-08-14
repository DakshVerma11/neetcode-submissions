class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Suffix sum for quick calculation of remaining stones
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        dp={}
        def dfs(idx: int, X: int) -> int:
            if (idx,X) in dp:
                return dp[(idx,X)]
            if idx >= n:
                return 0
            
            # If we can take all remaining piles
            if idx + X >= n:
                dp[(idx,X)]=suffix_sum[idx]
                return dp[(idx,X)]
            
            best = 0
            cur = 0
            for i in range(1, min(X, n - idx) + 1):
                cur += piles[idx + i - 1]
                # Current player gets cur + (remaining - opponent's best)
                remaining = suffix_sum[idx + i] - dfs(idx + i, max(X, 2 * i))
                best = max(best, cur + remaining)
            dp[(idx,X)]=best
            return best
        
        return dfs(0, 2)