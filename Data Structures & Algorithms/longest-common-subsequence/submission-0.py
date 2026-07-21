class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)

        lcs=[[0]*(m+1) for _ in range(n+1)]
        

        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    lcs[i+1][j+1]=lcs[i][j]+1
                else:
                    lcs[i+1][j+1]=max(lcs[i+1][j],lcs[i][j+1])
        return lcs[n][m]
        