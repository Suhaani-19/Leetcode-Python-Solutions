class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 0 or sum > num * 9:
            return ""
        
        res = []
        rem_sum = sum
        
        for i in range(num):
            # Remaining positions after current
            rem_slots = num - 1 - i
            
            # The maximum digit we can place here is 9, 
            # but we can't take a digit such that the remaining sum exceeds rem_slots * 9 
            # (Wait, if rem_sum is too small, we take what we need. If rem_sum is large, we take as much as possible).
            # Actually, to maximize score, we want large digits. Can we always take min(9, rem_sum)?
            # Yes, because any leftover sum can just be distributed among the remaining slots.
            # Let's check: if we take `cur`, the remaining sum `rem_sum - cur` must be <= rem_slots * 9.
            # Therefore, cur >= rem_sum - rem_slots * 9.
            
            low = max(0, rem_sum - rem_slots * 9)
            high = min(9, rem_sum)
            
            # To maximize the integer value while achieving the same maximum score components,
            # we pick the highest possible valid digit for the current most-significant position.
            cur = high
            res.append(str(cur))
            rem_sum -= cur
            
        return "".join(res)