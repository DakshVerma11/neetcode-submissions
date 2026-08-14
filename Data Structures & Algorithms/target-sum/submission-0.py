class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp={}
        def dfs(idx,cur):
            if idx==n:
                dp[(idx,cur)]=1 if cur==target else 0
            if (idx,cur) in dp:
                return dp[(idx,cur)]
            dp[(idx,cur)]=(dfs(idx+1,cur+nums[idx])+dfs(idx+1,cur-nums[idx]))
            return dp[(idx,cur)]
        return dfs(0,0)
