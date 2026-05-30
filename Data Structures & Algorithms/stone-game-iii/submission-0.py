class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)

        dp=[float('-inf')]* (n+1)

        dp[n]=0

        for i in range(n-1,-1,-1):
            cur=0
            for j in range(i,i+3 if i+3<n else n):
                cur+=stoneValue[j]
                dp[i]=max(dp[i],cur-dp[j+1])

        result = dp[0]
        if result == 0:
            return "Tie"
        return "Alice" if result > 0 else "Bob"