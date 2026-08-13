class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS=len(obstacleGrid)
        COLS=len(obstacleGrid[0])
        for i in range(COLS):
            if obstacleGrid[0][i]:
                break
            obstacleGrid[0][i]=-1

        for i in range(ROWS):
            if obstacleGrid[i][0]==1:
                break
            obstacleGrid[i][0]=-1
        print(obstacleGrid)

        for r in range(1,ROWS):
            for c in range(1,COLS):
                if obstacleGrid[r][c]:
                    continue
                if obstacleGrid[r-1][c]<1:
                    obstacleGrid[r][c]+=obstacleGrid[r-1][c]
                if obstacleGrid[r][c-1]<1:
                    obstacleGrid[r][c]+=obstacleGrid[r][c-1]
        print(obstacleGrid)
        return -obstacleGrid[ROWS-1][COLS-1] if obstacleGrid[ROWS-1][COLS-1]<0 else 0