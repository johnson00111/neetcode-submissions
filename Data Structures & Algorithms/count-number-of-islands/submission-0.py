class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        def dfs(x, y):
            if 0 > x or x > m-1 or 0 > y or y > n-1 or grid[x][y] == "0":
                return
            else:
                grid[x][y] = "0"
                for dx, dy in dirs:
                    dfs(x+dx, y+dy)

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans