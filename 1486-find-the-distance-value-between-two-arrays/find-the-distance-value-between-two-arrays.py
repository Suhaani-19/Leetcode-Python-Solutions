import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        distance_count = 0
        n2 = len(arr2)
        
        for val in arr1:
            # Find the insertion point to maintain sorted order
            idx = bisect.bisect_left(arr2, val)
            
            # Check the closest elements on the left and right of `idx`
            valid = True
            if idx < n2 and abs(arr2[idx] - val) <= d:
                valid = False
            if idx > 0 and abs(arr2[idx - 1] - val) <= d:
                valid = False
                
            if valid:
                distance_count += 1
                
        return distance_count