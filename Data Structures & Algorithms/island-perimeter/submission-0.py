class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        col=len(grid[0])
        p=0
        for i in range(rows):
            for j in range(col):
                if grid[i][j]==1:
                    p+=4
                    if i>0 and grid[i-1][j]==1:
                        p-=2
                    if j>0 and grid[i][j-1]==1:
                        p-=2
        return p
                
