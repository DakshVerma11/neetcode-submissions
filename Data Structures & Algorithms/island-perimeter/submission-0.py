class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=0
        R=len(grid)
        C=len(grid[0])
        for row in range(R):
            for col in range(C):
                if grid[row][col]:
                    curp=4
                    if row-1>=0:
                        if grid[row-1][col]:
                            curp-=1
                    if col-1>=0:
                        if grid[row][col-1]:
                            curp-=1
                    if row+1<R:
                        if grid[row+1][col]:
                            curp-=1
                    if col+1<C:
                        if grid[row][col+1]:
                            curp-=1
                    #print(row,' , ',col,' = ',curp)
                    perimeter+=curp
        return perimeter