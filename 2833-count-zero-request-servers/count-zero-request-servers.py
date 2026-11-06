class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time
        logs.sort(key=lambda item: item[1])
        
        # Sort queries while preserving their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        server_counts = {}
        active_servers = 0
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for orig_idx, q in sorted_queries:
            window_start = q - x
            window_end = q
            
            # Expand the window to include all logs up to time `q`
            while right < num_logs and logs[right][1] <= window_end:
                server_id = logs[right][0]
                if server_counts.get(server_id, 0) == 0:
                    active_servers += 1
                server_counts[server_id] = server_counts.get(server_id, 0) + 1
                right += 1
                
            # Shrink the window from the left to remove logs older than `q - x`
            while left < num_logs and logs[left][1] < window_start:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    active_servers -= 1
                left += 1
                
            # Zero-request servers = total servers - active servers
            ans[orig_idx] = n - active_servers
            
        return ans