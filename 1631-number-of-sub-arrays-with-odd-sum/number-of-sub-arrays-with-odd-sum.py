class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # Base case: prefix sum 0 is even
        prefix_sum = 0
        ans = 0
        
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 != 0:
                ans += even_count
                odd_count += 1
            else:
                ans += odd_count
                even_count += 1
                
        return ans % MOD