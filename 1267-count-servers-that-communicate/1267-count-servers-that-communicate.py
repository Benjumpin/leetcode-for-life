class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r_count = [0] * m
        c_count = [0] * n
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    r_count[r] += 1
                    c_count[c] += 1

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r_count[r] > 1 or c_count[c] > 1:
                        ans += 1

        return ans


        