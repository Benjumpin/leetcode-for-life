import heapq
from sortedcontainers import SortedSet

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Available servers (0 to k-1)
        ts = SortedSet(range(k))

        # Min-heap of busy servers: (finish_time, server_id)
        busy = []  

        count = [0] * k

        for i, start in enumerate(arrival):
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)
                ts.add(server_id)

            # dropping req
            if not ts:
                continue
            
            # pref server
            target = i % k
            
            # find next avai server
            idx = ts.bisect_left(target)

            # wrap ard to smallest avai server
            if idx == len(ts):
                idx = 0

            # assign req to selected server
            server = ts.pop(idx)
            count[server] += 1
            
            # cal req complete time
            heapq.heappush(busy, (start + load[i], server))

        max_req = max(count)
        
        result = []
        for s_id, req_count in enumerate(count):
            if req_count == max_req:
                result.append(s_id)

        return result