class Solution:

    def smallestIndex(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            if sum(int(digit) for digit in str(num)) == i:
                return i
        return -1