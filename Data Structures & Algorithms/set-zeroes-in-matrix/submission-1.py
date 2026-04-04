class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R,C= len(matrix[0]),len(matrix)
        setzero=set()
        for r in range(R):
            for c in range(C):
                if matrix[c][r]==0:
                    setzero.add(tuple([r,c]))
        
        for row,col in setzero:
            for i in range(R):
                matrix[col][i]=0
            for i in range(C):
                matrix[i][row]=0
        return

        