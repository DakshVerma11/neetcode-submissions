class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t=sum(nums)
        if t%2!=0:
            return False
        t//=2
        n=len(nums)
        def dfs(i,cursum):
            if cursum==t:
                return True
            if i>=n or cursum>t:
                return False
            return dfs(i+1,cursum+nums[i]) or dfs(i+1,cursum)

        return dfs(0,0)