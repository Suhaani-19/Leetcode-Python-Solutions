from typing import List
from functools import cache
from itertools import accumulate


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        """
        Stone Game V: Alice and Bob play a game with stones in a row.
        Each turn, a player divides stones into two non-empty groups.
        The player with smaller sum gets points equal to that sum.
        If sums are equal, player chooses which sum to take as points.
        Returns maximum points Alice can get with optimal play.
        """
      
        @cache
        def dp(left: int, right: int) -> int:
            """
            Dynamic programming function to find maximum score in range [left, right].
          
            Args:
                left: Starting index of the range (inclusive)
                right: Ending index of the range (inclusive)
          
            Returns:
                Maximum score achievable from stones in range [left, right]
            """
            # Base case: if range is invalid or contains single stone, no score
            if left >= right:
                return 0
          
            max_score = 0
            left_sum = 0
            # Calculate right sum using prefix sum array
            right_sum = prefix_sum[right + 1] - prefix_sum[left]
          
            # Try all possible split points
            for split_point in range(left, right):
                # Update sums after including current stone in left group
                left_sum += stoneValue[split_point]
                right_sum -= stoneValue[split_point]
              
                if left_sum < right_sum:
                    # Left group has smaller sum, Alice gets left_sum points
                    # Pruning: skip if current max_score is already >= 2 * left_sum
                    if max_score >= left_sum * 2:
                        continue
                    max_score = max(max_score, left_sum + dp(left, split_point))
                  
                elif left_sum > right_sum:
                    # Right group has smaller sum, Alice gets right_sum points
                    # Pruning: break early if max_score is already >= 2 * right_sum
                    if max_score >= right_sum * 2:
                        break
                    max_score = max(max_score, right_sum + dp(split_point + 1, right))
                  
                else:
                    # Both groups have equal sum, Alice chooses the better option
                    max_score = max(
                        max_score,
                        max(left_sum + dp(left, split_point), 
                            right_sum + dp(split_point + 1, right))
                    )
          
            return max_score
      
        # Build prefix sum array for efficient range sum queries
        # prefix_sum[i] = sum of stoneValue[0:i]
        prefix_sum = list(accumulate(stoneValue, initial=0))
      
        # Start the recursive solution from the entire array
        return dp(0, len(stoneValue) - 1)
