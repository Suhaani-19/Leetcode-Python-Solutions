class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        # Pair each number with its (digit_sum, value, original_index)
        arr = []
        for i, val in enumerate(nums):
            arr.append((digit_sum(val), val, i))
        
        # Sort based on digit sum, then value
        arr.sort(key=lambda x: (x[0], x[1]))
        
        # Find minimum swaps using cycle detection
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue
            
            # Count the size of the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps