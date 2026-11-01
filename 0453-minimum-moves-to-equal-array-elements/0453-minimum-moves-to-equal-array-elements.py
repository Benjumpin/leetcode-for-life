class Solution:
    def minMoves(self, nums):
        # if len(set(nums)) == 1:
        #     return 0
        # ans = 0
        # small = min(nums)
        # for i in nums:
        #     ans += i - small
        # print(ans)
        # return ans  
        return sum(nums) - min(nums) * len(nums)