class Solution:
    def minMoves2(self, nums: list[int]) -> int:   
        nums.sort()
        mid = nums[len(nums)//2]
        # ans = 0
        # for i in nums:
        #     ans += abs(mid - i)
        #     print(abs(mid - i))
        return sum(abs(mid - i) for i in nums)
         
        