class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp=[defaultdict(int) for _ in range(n+1)]
        dp[n][target]=1
        def dfs(idx,cur):
            if idx==n or cur in dp[idx]:
                return dp[idx][cur]
            #print(idx,cur)
            dp[idx][cur]=(dfs(idx+1,cur+nums[idx])+dfs(idx+1,cur-nums[idx]))
            return dp[idx][cur]
        
        return dfs(0,0)
