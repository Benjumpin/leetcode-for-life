import math
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] ** 2
        
        n = len(nums)
        pos = n - n//2
        neg = n//2 
        sum = 0

        for i in range(len(nums)): #O(n)
            nums[i] = abs(nums[i])
 
        nums.sort() #O(nlogn)
        # print(nums)
        for i in range(pos): # pos
            sum += nums.pop() ** 2
        for i in range(neg):
            sum -= nums[i] ** 2
        
        return sum
        