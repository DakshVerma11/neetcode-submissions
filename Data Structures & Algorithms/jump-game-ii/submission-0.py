class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[n*1001 for i in range(n)]
        dp[n-1]=0
        #store the number of jumps till n-1

        for i in range(n-2,-1,-1):
            j=nums[i]
            minJumps=n*1001
            if i+j>=n:
                j=n-1-i
            while j:
                minJumps=min(minJumps,dp[i+j])
                j-=1
            dp[i]=1+minJumps
            
        return dp[0]