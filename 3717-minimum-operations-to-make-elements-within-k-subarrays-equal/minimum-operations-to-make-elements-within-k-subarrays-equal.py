from sortedcontainers import SortedList
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        minOps = self.getMinOps(nums, x)

        INF = float('inf')
        mem = [[-1] * (k + 1) for _ in range(n + 1)]

        def dp(i, k):
            if k == 0:
                return 0
            if i == n:
                return INF
            if mem[i][k] != -1:
                return mem[i][k]

            skip = dp(i + 1, k)

            pick = INF
            if i + x <= n:
                pick = minOps[i] + dp(i + x, k - 1)

            mem[i][k] = min(skip, pick)
            return mem[i][k]

        return dp(0, k)

    def getMinOps(self, nums: List[int], x: int) -> List[int]:
        lower = SortedList()
        upper = SortedList()

        lowerSum = 0
        upperSum = 0

        minOps = []

        for i, num in enumerate(nums):
            # Insert the new element
            if not lower or num <= lower[-1]:
                lower.add(num)
                lowerSum += num
            else:
                upper.add(num)
                upperSum += num

            # Remove the element outside the window
            if i >= x:
                outNum = nums[i - x]

                if outNum in lower:
                    lower.remove(outNum)
                    lowerSum -= outNum
                else:
                    upper.remove(outNum)
                    upperSum -= outNum

            # Balance the two halves
            if len(lower) < len(upper):
                val = upper.pop(0)
                lower.add(val)
                upperSum -= val
                lowerSum += val

            elif len(lower) - len(upper) > 1:
                val = lower.pop(-1)
                upper.add(val)
                lowerSum -= val
                upperSum += val

            # Calculate operations for the current window
            if i >= x - 1:
                median = lower[-1]

                ops = (
                    median * len(lower) - lowerSum
                    + upperSum - median * len(upper)
                )

                minOps.append(ops)

        return minOps