import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1  # Any single element has prod = x, gcd = x, lcm = x -> x == x * x is only for 1, but constraint n >= 2
        
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = x if g == 0 else math.gcd(g, x)
                l = math.lcm(l, x)
                
                if prod == l * g:
                    ans = max(ans, j - i + 1)
                
                # Since gcd only decreases and lcm is bounded by 2520,
                # once prod is already huge, it won't catch up to l * g.
                if prod > 2520 * 2520:
                    break
                    
        return ans