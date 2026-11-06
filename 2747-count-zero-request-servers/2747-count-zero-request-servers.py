from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda log: log[1])

        q_sorted = sorted((q, idx) for idx, q in enumerate(queries))

        ans = [0] * len(queries)
        
        hmap = defaultdict(int)

        l, r = 0, 0
        n_logs = len(logs)
        
        for q, i in q_sorted:
            wind_l = q - x
            wind_r = q

            while r < n_logs and logs[r][1] <= wind_r:
                server = logs[r][0]
                hmap[server] += 1
                r += 1

            while l < n_logs and logs[l][1] < wind_l:
                server = logs[l][0]
                hmap[server] -= 1
                if hmap[server] == 0:
                    del hmap[server]
                l += 1

            ans[i] = n - len(hmap)

        return ans


        