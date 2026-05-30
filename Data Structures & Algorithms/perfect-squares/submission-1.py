class Solution:
    def numSquares(self, n: int) -> int:
        sqrsAvailable=[]
        for i in range(1,math.ceil(math.sqrt(n))+1):
            sqrsAvailable.append(i*i)
        #print(sqrsAvailable)


        dp=[n+1]*(n+1)
        dp[0]=0

        for i in range(n+1):
            for sqr in sqrsAvailable:
                #print('here')
                if i>=sqr:
                    #print(i,'#',sqr)
                    dp[i]=min(dp[i],1+dp[i-sqr])
        #print(dp)
        return dp[n]