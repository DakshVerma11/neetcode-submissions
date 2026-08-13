class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=(total+1)//2
        #print(total,target)
        dp={}
        def dfs(i, cur):
            #print(i,cur)
            if (i,cur) in dp:
                return dp[(i,cur)]
            if cur>=target or i==len(stones):
                dp[(i,cur)]=abs(2*cur-total)
                return dp[(i,cur)]
            dp[(i, cur)] = min(
                dfs(i + 1, cur),
                dfs(i + 1, cur + stones[i])
            )
            return dp[(i, cur)]
        return dfs(0,0)