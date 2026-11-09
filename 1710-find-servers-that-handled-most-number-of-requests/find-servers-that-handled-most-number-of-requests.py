from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap to store (free_time, server_id) for currently busy servers
        busy_servers = []
        
        # SortedList to keep track of all currently available server IDs
        available_servers = SortedList(range(k))
        
        # Array to count how many requests each server has handled
        request_counts = [0] * k
        
        for i, (arr_time, l) in enumerate(zip(arrival, load)):
            # 1. Free up servers whose tasks have finished by the current arrival time
            while busy_servers and busy_servers[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy_servers)
                available_servers.add(server_id)
            
            # 2. If no servers are available, drop the request
            if not available_servers:
                continue
            
            # 3. Find the first available server >= (i % k)
            target = i % k
            idx = available_servers.bisect_left(target)
            
            # If no server >= target is available, wrap around to the first available server (index 0)
            if idx == len(available_servers):
                idx = 0
            
            server_id = available_servers[idx]
            
            # 4. Assign the request to this server
            available_servers.remove(server_id)
            heapq.heappush(busy_servers, (arr_time + l, server_id))
            request_counts[server_id] += 1
            
        # 5. Find the maximum number of requests handled by any server
        max_handled = max(request_counts)
        
        # 6. Return all servers that handled the maximum number of requests
        return [i for i, count in enumerate(request_counts) if count == max_handled]