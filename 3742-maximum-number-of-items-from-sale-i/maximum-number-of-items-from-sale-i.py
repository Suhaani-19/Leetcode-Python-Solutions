from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        # Precompute how many other items j != i have factor_j divisible by factor_i
        bonus = [0] * n
        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            bonus[i] = cnt

        dp = [0] * (budget + 1)

        for i in range(n):
            _, price = items[i]
            if price > budget:
                continue

            extra_gain = bonus[i]

            # Additional copies of item i (after the first): +1 item per `price` spent
            for b in range(price, budget + 1):
                if dp[b - price] + 1 > dp[b]:
                    dp[b] = dp[b - price] + 1

            # First copy of item i: +1 purchased + `extra_gain` free items
            first_gain = 1 + extra_gain
            for b in range(budget, price - 1, -1):
                if dp[b - price] + first_gain > dp[b]:
                    dp[b] = dp[b - price] + first_gain

        return max(dp)