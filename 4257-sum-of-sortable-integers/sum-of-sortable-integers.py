class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = 0
        
        # Precompute string representations of each block and target if numbers can be large,
        # or use a linear-time rotation check (Min-Expressing algorithm / Duval's or KMP)
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            
            is_valid = True
            for i in range(0, n, k):
                block = nums[i:i+k]
                target = sorted_nums[i:i+k]
                
                if sorted(block) != sorted(target):
                    is_valid = False
                    break
                
                # Fast cyclic rotation check using string concatenation search
                # To avoid ambiguity with numbers (e.g., '12' vs '1' and '2'), 
                # convert elements to strings with a delimiter or use Duval's algorithm / KMP.
                # Since integers might vary in digit length, using a tuple or comma-separated string:
                block_str = ",".join(map(str, block))
                target_str = ",".join(map(str, target))
                
                if target_str not in (block_str + "," + block_str):
                    is_valid = False
                    break
            
            if is_valid:
                ans += k
                
        return ans