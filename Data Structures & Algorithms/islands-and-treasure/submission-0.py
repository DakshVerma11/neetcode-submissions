class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS=len(grid)
        COLS=len(grid[0])

        def dfs(r,c,dist):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]==-1 or grid[r][c]<dist:
                return

            grid[r][c]=dist
            dfs(r+1,c,dist+1)
            dfs(r,c+1,dist+1)
            dfs(r-1,c,dist+1)
            dfs(r,c-1,dist+1)

            
        for i in range(ROWS):
            for j in range(COLS):
                if not grid[i][j]:
                    dfs(i,j,0)
        
        return
        
            