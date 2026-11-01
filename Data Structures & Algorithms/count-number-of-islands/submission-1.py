class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        islands = 0
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(r,c):
            if(r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for dr,dc in dirs:
                dfs(dr+r,dc+c)

        def bfs(r,c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r,c))

            while queue:
                i,j = queue.popleft()
                for dr,dc in dirs:
                    nr, nc = dr+i, dc+j
                    if(nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]=="0"):
                        continue
                    if grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr,nc))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    # dfs(i,j)
                    bfs(i,j)
                    islands += 1
        return islands