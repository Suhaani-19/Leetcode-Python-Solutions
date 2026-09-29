from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
        
        # Starting cell must be '(' and ending cell must be ')'
        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        @cache
        def dfs(r: int, c: int, balance: int) -> bool:
            # Update balance for current cell
            balance += 1 if grid[r][c] == '(' else -1
            
            # If balance drops below 0, sequence is invalid
            if balance < 0:
                return False
            
            # Reached destination: balance must be 0
            if r == m - 1 and c == n - 1:
                return balance == 0
            
            # Explore moving right or down
            if c + 1 < n and dfs(r, c + 1, balance):
                return True
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
                
            return False

        return dfs(0, 0, 0)