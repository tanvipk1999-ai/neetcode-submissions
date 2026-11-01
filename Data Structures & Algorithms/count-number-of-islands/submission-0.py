class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr,nc = len(grid),len(grid[0])
        islands = 0
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if(r<0 or c<0 or r>=nr or c>=nc or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for dr,dc in dirs:
                dfs(dr+r,dc+c)
            
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands += 1
        return islands