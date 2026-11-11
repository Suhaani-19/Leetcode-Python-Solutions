class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Determine how many items are needed for both requirements simultaneously
        common = min(need1, need2)
        
        # Cost for satisfying the overlapping amount
        total_cost = common * min(costBoth, cost1 + cost2)
        
        # Remaining requirements after covering the common part
        rem1 = need1 - common
        rem2 = need2 - common
        
        # If type 1 still has a remaining requirement
        if rem1 > 0:
            total_cost += rem1 * min(cost1, costBoth)
            
        # If type 2 still has a remaining requirement
        if rem2 > 0:
            total_cost += rem2 * min(cost2, costBoth)
            
        return total_cost