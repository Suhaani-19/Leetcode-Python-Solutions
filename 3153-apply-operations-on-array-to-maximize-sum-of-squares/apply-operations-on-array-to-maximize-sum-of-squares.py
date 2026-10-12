class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        
        # Count set bits for each position
        for num in nums:
            for i in range(31):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        # Construct the k largest numbers greedily
        max_nums = [0] * k
        for i in range(k):
            current_num = 0
            for bit in range(31):
                if bit_counts[bit] > 0:
                    current_num |= (1 << bit)
                    bit_counts[bit] -= 1
            max_nums[i] = current_num
            
        # Calculate sum of squares modulo 10^9 + 7
        ans = sum(x * x for x in max_nums) % MOD
        return ans