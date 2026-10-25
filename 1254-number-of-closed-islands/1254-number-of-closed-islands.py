class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        n = len(grid)
        m = len(grid[0])

        outside = n * m
        uf = UFDS(n * m + 1) # extra 1 for boundary node (to check if nodes touches boundary)
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    continue
                # give index to each cell (0 - n*m-1), outside index (n*m)
                index = r * m + c

                if r == 0 or r == n - 1 or c == 0 or c == m - 1: 
                    # check if land cell at boundary value
                    uf.union(index, outside)

                # union neighbour (below)
                if r + 1 < n and grid[r + 1][c] == 0:
                    uf.union(index, (r + 1) * m + c)

                # union neighbour (right)
                if c + 1 < m and grid[r][c + 1] == 0:
                    uf.union(index, r * m + (c + 1))      
        
        outside_root = uf.find(outside)
        island_root = set()

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    index = r * m + c
                    root = uf.find(index)

                    if root != outside_root:
                        island_root.add(root)

        return len(island_root)