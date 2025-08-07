class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 2025-08-06
        m = len(grid) # row
        n = len(grid[0]) # column

        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        def dfs(i,j):
            if visited[i][j]:
                return
            visited[i][j] = True
            if grid[i][j] == '0':
                return
            else: # explore up, down, left, right
                if i > 0:
                    dfs(i-1,j)
                if i < m-1:
                    dfs(i+1,j)
                if j > 0:
                    dfs(i,j-1)
                if j < n-1:
                    dfs(i, j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i,j)
        return count