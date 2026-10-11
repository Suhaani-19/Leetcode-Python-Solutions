class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # Iterate through the array using 1-based indexing
        for i in range(1, n + 1):
            if n % i == 0:
                # Add the square of the element (adjusting for 0-based Python indexing)
                total_sum += nums[i - 1] ** 2
                
        return total_sum