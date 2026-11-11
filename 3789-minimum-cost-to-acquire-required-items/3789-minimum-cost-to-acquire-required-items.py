class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 + need2 == 0:
            return 0 
        
        cost = 0

        if need1 <= need2:
            cost = need1 * min(costBoth, cost1 + cost2) + (need2 - need1) * min(costBoth, cost2)
        
        else: 
            cost = need2 * min(costBoth, cost1 + cost2) + (need1 - need2) * min(costBoth, cost1)
        
        return cost