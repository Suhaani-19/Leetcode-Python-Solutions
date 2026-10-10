class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        
        # Calculate absolute differences for each index
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        # Count frequencies of each difference value
        max_diff = max(diffs)
        if max_diff == 0:
            return 0
        
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
            
        # Reduce differences from highest to lowest using available k
        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue
            
            if k >= count[d]:
                # Reduce all current 'd' elements down to 'd - 1'
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                # Reduce as many 'd' elements as possible down to 'd - 1'
                count[d - 1] += k
                count[d] -= k
                k = 0
                break
                
        # Calculate final sum of squared differences
        return sum(c * (d ** 2) for d, c in enumerate(count))