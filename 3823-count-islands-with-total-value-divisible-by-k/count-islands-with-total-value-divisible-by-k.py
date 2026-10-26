class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and (r, c) not in visited:
                    # BFS or DFS to find the total sum of the island
                    current_sum = 0
                    queue = [(r, c)]
                    visited.add((r, c))
                    
                    while queue:
                        curr_r, curr_c = queue.pop(0)
                        current_sum += grid[curr_r][curr_c]
                        
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0 and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
                                
                    if current_sum % k == 0:
                        count += 1
                        
        return count