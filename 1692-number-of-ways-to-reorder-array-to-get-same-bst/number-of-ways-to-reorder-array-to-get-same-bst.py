class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Number of ways to interleave left and right subtrees
            # is combinations(len(left) + len(right), len(left))
            ways_root = comb(len(left) + len(right), len(left), MOD)
            
            return (ways_root * helper(left) * helper(right)) % MOD

        def comb(n, k, mod):
            return math.comb(n, k) % mod

        return (helper(nums) - 1 + MOD) % MOD