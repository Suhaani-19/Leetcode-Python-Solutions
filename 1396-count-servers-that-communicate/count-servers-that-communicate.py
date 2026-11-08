class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        row_counts = [0] * rows
        col_counts = [0] * cols
        
        # Step 1: Count servers in each row and column
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
                    
        # Step 2: Count servers that can communicate
        communicating_servers = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        communicating_servers += 1
                        
        return communicating_servers