class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        #     [1,2,3,4]
        # step 1 2 3 4
        # from 0 to 1 = 1 + (1-0)^2 = 2
        # from 0 to 2 = 2 + (2-0)^2 = 6
        # from 0 to 3 = 3 + (3-0)^2 = 12
        
        # from 1 to 2 = 2 + (2-1)^2 = 3
        # from 1 to 3 = 3 + (3-1)^2 = 7
        # from 1 to 4 = 4 + (4-1)^2 = 13

        # from 2 to 3 = 3 + (3-2)^2 = 4
        # from 2 to 4 = 4 + (4-2)^2 = 8

        # from 3 to 4 = 4 + (4-3)^2 = 5


        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for j in range(1, n + 1):
            for i in range(max(0, j-3), j):
                dp[j] = min(dp[j] ,dp[i] + costs[j-1] + (j-i)**2)
        return dp[n]