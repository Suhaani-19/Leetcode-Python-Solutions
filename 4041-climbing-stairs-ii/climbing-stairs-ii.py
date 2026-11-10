class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[j] stores the minimum cost to reach step j.
        # Note: costs is 1-indexed in the problem statement, so costs[j-1] corresponds to step j.
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for j in range(1, n + 1):
            # Try all valid previous steps: j - 1, j - 2, j - 3
            for i in range(max(0, j - 3), j):
                jump_cost = costs[j - 1] + (j - i) ** 2
                dp[j] = min(dp[j], dp[i] + jump_cost)
                
        return dp[n]