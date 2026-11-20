from collections import defaultdict
from typing import List


class Solution:

  def maxSelectedElements(self, nums: List[int]) -> int:
    nums.sort()
    dp = defaultdict(int)
    ans = 0

    for x in nums:
      # Option 1: increase x to x + 1, extending a sequence ending at x
      dp[x + 1] = max(dp[x + 1], dp[x] + 1)
      # Option 2: keep x as x, extending a sequence ending at x - 1
      dp[x] = max(dp[x], dp[x - 1] + 1)

      ans = max(ans, dp[x], dp[x + 1])

    return ans