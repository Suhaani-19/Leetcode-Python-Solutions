from collections import Counter
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Double hashing parameters to avoid collisions
        MOD1, MOD2 = 10**9 + 7, 10**9 + 9
        BASE1, BASE2 = 1315423911, 2654435761
        
        # Precompute prefix hashes and powers
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        
        for i, x in enumerate(nums):
            p1[i + 1] = (p1[i] * BASE1) % MOD1
            p2[i + 1] = (p2[i] * BASE2) % MOD2
            h1[i + 1] = (h1[i] * BASE1 + x) % MOD1
            h2[i + 1] = (h2[i] * BASE2 + x) % MOD2
            
        def has_unique_subarray(length: int) -> bool:
            counts = Counter()
            pw1, pw2 = p1[length], p2[length]
            
            for i in range(n - length + 1):
                j = i + length
                sub_h1 = (h1[j] - h1[i] * pw1) % MOD1
                sub_h2 = (h2[j] - h2[i] * pw2) % MOD2
                counts[(sub_h1, sub_h2)] += 1
                
            return any(freq == 1 for freq in counts.values())

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique_subarray(mid):
                hi = mid
            else:
                lo = mid + 1
                
        return lo