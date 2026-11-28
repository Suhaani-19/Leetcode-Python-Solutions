
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Step 1: Count frequency of each factor
        freq = [0] * (n + 1)
        min_price = float('inf')

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        # Step 2: Count items whose factors are multiples
        for i in range(1, n + 1):
            for j in range(2 * i, n + 1, i):
                freq[i] += freq[j]

        # Step 3: Calculate profitable free-item opportunities
        opportunities = {}

        for factor, price in items:
            gain = freq[factor] - 1

            if gain > 0 and price <= 2 * min_price:
                opportunities[price] = opportunities.get(price, 0) + gain

        # Step 4: Greedily buy the cheapest double-value items
        ans = 0

        for price in sorted(opportunities):
            count = min(opportunities[price], budget // price)

            ans += 2 * count
            budget -= price * count

        # Step 5: Spend remaining budget on cheapest items
        ans += budget // min_price

        return ans
