class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # If out of bounds, it means the island touches the boundary
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            # If it's water (1) or already visited, return True (no boundary touched so far from this branch)
            if grid[r][c] == 1:
                return True
            
            # Mark the current cell as visited by turning it into water (1)
            grid[r][c] = 1
            
            # Check all 4 directions and ensure all parts stay within bounds (do not touch border)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            
            return left and right and up and down

        closed_islands_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # If DFS returns True, no cell in this component touched the boundary
                    if dfs(r, c):
                        closed_islands_count += 1
                        
        return closed_islands_count