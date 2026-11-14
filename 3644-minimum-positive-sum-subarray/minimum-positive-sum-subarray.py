class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        # Check all possible starting points for the subarray
        for i in range(n):
            current_sum = 0
            # Consider lengths from l to r
            for j in range(i, min(n, i + r)):
                current_sum += nums[j]
                # Subarray length is (j - i + 1)
                if (j - i + 1) >= l and current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    
        return min_sum if min_sum != float('inf') else -1