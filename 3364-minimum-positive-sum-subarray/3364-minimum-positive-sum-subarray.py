class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float("inf")
        for window in range(l, r + 1):
            for idx in range(n - window + 1):
                temp = sum(nums[idx : idx + window])
                if 0 < temp < ans:
                    ans = temp
        if ans == float("inf"):
            ans = -1
        return ans 
            
                




