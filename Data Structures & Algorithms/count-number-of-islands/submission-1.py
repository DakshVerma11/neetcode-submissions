class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        directions=[[-1,0],[0,-1],[1,0],[0,1]]
        count=0
        def dfs(i,j):
            if i<0 or j<0 or i>=ROWS or j>=COLS:
                return
            
            if grid[i][j]=='0':
                return
            grid[i][j]='0'
            for dx,dy in directions:
                dfs(i+dx,j+dy)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]=='1':
                    count+=1
                    dfs(row,col)
        return count