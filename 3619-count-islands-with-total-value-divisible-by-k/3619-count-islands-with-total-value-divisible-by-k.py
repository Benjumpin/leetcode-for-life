class Solution:
  
    def dfs(self, grid, row, col) -> int: 
        n = len(grid)
        m = len(grid[0])

        if (row < 0 or col < 0 or row >= n or col >= m or grid[row][col] == 0):
            return 0
        val = grid[row][col]
        grid[row][col] = 0
        total = val
        total += self.dfs(grid, row + 1, col)
        total += self.dfs(grid, row - 1, col)
        total += self.dfs(grid, row, col + 1)
        total += self.dfs(grid, row, col - 1)

        return total 

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        for r in range(n):
            for c in range(m):

                if (grid[r][c] > 0):
                    sum = self.dfs(grid, r, c)
                    if (sum % k == 0):
                        count += 1
        return count
        