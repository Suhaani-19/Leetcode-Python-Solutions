import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list: u -> list of (v, w)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Min-heap to store (distance, node, consecutive_count)
        # Start at node 0 with count 1 for labels[0]
        pq = [(0, 0, 1)]
        
        # Distance dictionary/matrix to track the minimum weight to reach (node, count)
        # Using a hash map to handle sparse states efficiently
        min_dist = {}
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            # If we reached the target node, return the distance
            if u == n - 1:
                return d
                
            if (u, count) in min_dist and min_dist[(u, count)] < d:
                continue
                
            for v, w in adj[u]:
                # Calculate new consecutive count for node v
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1
                    
                # Skip if it violates the constraint
                if new_count > k:
                    continue
                    
                new_dist = d + w
                
                # If we found a shorter way to reach state (v, new_count)
                if (v, new_count) not in min_dist or new_dist < min_dist[(v, new_count)]:
                    min_dist[(v, new_count)] = new_dist
                    heapq.heappush(pq, (new_dist, v, new_count))
                    
        return -1