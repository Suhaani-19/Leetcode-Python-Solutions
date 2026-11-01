class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val = min(nums)
        return sum(nums) - min_val * len(nums)