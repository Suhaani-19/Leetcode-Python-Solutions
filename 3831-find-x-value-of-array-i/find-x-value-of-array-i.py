class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k  # dp[r] stores count of subarrays ending at current index with product % k == r
        
        for num in nums:
            rem = num % k
            next_dp = [0] * k
            
            # Subarray consisting of just the current element
            next_dp[rem] += 1
            
            # Extend existing subarrays
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * rem) % k] += dp[r]
            
            # Accumulate counts into the final answer
            for r in range(k):
                result[r] += next_dp[r]
                
            dp = next_dp
            
        return result