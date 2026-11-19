class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        return min(
            nums[n - 1] - nums[2],  # change 2 smallest
            nums[n - 3] - nums[0],  # change 2 largest
            nums[n - 2] - nums[1],  # change 1 smallest & 1 largest
        )