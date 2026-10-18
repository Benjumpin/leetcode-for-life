from typing import List
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n  = len(nums)

        # Pascal triangle for quick combination computation 
        # |   0  1  2  3 |   3 C 2 = 3
        # |0 [1]         |   2 C 1 = 1
        # |1 [1][1]      |   3 C 0 = 1
        # |2 [1][2][1]   |
        # |3 [1][3][3][1]|
        
        combi =[[0] * (n+1) for _ in range(n+1)]
        
        for i in range(n+1):
            combi[i][0] = combi[i][i] = 1
            for j in range(1,i):
                combi[i][j] = (combi[i-1][j-1] + combi[i-1][j]) % MOD
        
        def get_ways(sub_nums: List[int]) -> int:
            if len(sub_nums) <= 2:
                # nums size 1 or 2 only have 1 possible combi
                return 1 

            root = sub_nums[0]
            left_subtree = [x for x in sub_nums[1:] if x < root]
            right_subtree = [x for x in sub_nums[1:] if x >= root]

            l_size = len(left_subtree)
            r_size = len(right_subtree)

            # Num ways to interleavve left and right subtress while preserving order * Num of ways to do the same in left tree * Num of ways to do the same in right tree
            
            ans = combi[l_size + r_size][l_size]
            ans = (ans * get_ways(left_subtree)) % MOD
            ans = (ans * get_ways(right_subtree)) % MOD
            
            return ans
        # remove original array from combinations
        return (get_ways(nums) - 1) % MOD