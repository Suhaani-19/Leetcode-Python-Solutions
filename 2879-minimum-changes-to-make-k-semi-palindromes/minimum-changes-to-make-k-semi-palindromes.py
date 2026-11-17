class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Step 1: Precompute all proper divisors for each length from 1 to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        # Step 2: Calculate cost[i][j] = min changes to make s[i...j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        # Helper to count changes to make a group a palindrome
        def get_palindrome_changes(sub):
            changes = 0
            l, r = 0, len(sub) - 1
            while l < r:
                if sub[l] != sub[r]:
                    changes += 1
                l += 1
                r -= 1
            return changes

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = float('inf')
                
                # Try every proper divisor d of the substring length
                for d in divisors[length]:
                    current_cost = 0
                    # Check each of the d groups
                    for start in range(d):
                        group_chars = []
                        for idx in range(i + start, i + length, d):
                            group_chars.append(s[idx])
                        current_cost += get_palindrome_changes(group_chars)
                    
                    min_changes = min(min_changes, current_cost)
                
                cost[i][j] = min_changes

        # Step 3: DP to partition into k semi-palindromes
        # dp[idx][parts] -> min changes for suffix s[idx:] with `parts` remaining
        memo = {}
        
        def dp(idx, parts):
            if parts == 1:
                return cost[idx][n - 1]
            if (idx, parts) in memo:
                return memo[(idx, parts)]
            
            res = float('inf')
            # Try all possible cut points for the next substring
            # We must leave enough characters for the remaining (parts - 1) substrings (each at least length 2)
            for next_idx in range(idx + 2, n - parts + 2):
                res = min(res, cost[idx][next_idx - 1] + dp(next_idx, parts - 1))
            
            memo[(idx, parts)] = res
            return res

        return dp(0, k)