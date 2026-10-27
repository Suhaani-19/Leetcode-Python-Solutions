class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for r in range(m):
            if r == 0:
                # The entire first row is free
                grid.append("." * n)
            else:
                # Only the last column is free for subsequent rows
                grid.append("#" * (n - 1) + ".")
        return grid