class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        while q and fresh>0:
            lq = len(q)
            for i in range(lq):
                ci,cj = q.popleft()
                for dr, dc in dirs:
                    nr = ci+dr
                    nc = cj+dc
                    if (nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            time +=1 
        return time if fresh == 0 else -1


        