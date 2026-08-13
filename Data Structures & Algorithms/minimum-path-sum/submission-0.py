class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if row>0 and col>0:
                    grid[row][col]+=min(grid[row-1][col],grid[row][col-1])
                elif row>0:
                    grid[row][col]+=grid[row-1][col]
                elif col>0:
                    grid[row][col]+=grid[row][col-1]
                
                #print(row,col,grid)
        #print(grid)
        return grid[ROWS-1][COLS-1]

