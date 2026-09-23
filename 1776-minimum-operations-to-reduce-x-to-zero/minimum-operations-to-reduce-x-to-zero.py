class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        # If total sum is less than x, it's impossible
        if target < 0:
            return -1
        # If total sum equals x, we need to remove all elements
        if target == 0:
            return len(nums)
        
        current_sum = 0
        left = 0
        max_len = -1
        
        # Sliding window to find the longest subarray summing to target
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink window from the left if sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            
            # Record maximum length when sum matches target
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return len(nums) - max_len if max_len != -1 else -1