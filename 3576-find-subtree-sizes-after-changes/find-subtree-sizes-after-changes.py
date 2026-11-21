from typing import List
from collections import defaultdict

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = defaultdict(list)
        for i in range(1, n):
            adj[parent[i]].append(i)
        
        new_parent = list(parent)
        last_seen = {}  # Tracks the closest ancestor for each character
        
        # Step 1: DFS on the original tree to find new parents simultaneously
        def find_parents(u: int):
            char = s[u]
            prev_node = last_seen.get(char, -1)
            
            # If a matching ancestor exists, update u's parent
            if prev_node != -1:
                new_parent[u] = prev_node
            
            # Update last_seen for u's children, then backtrack
            last_seen[char] = u
            for v in adj[u]:
                find_parents(v)
            last_seen[char] = prev_node
            
        find_parents(0)
        
        # Step 2: Build the modified tree using new_parent
        new_adj = defaultdict(list)
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        # Step 3: DFS on the new tree to calculate subtree sizes
        ans = [0] * n
        def count_sizes(u: int) -> int:
            size = 1
            for v in new_adj[u]:
                size += count_sizes(v)
            ans[u] = size
            return size
            
        count_sizes(0)
        return ans