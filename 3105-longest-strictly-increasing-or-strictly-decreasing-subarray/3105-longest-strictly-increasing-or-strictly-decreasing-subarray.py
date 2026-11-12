# tired code, try again when awake
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        up, u_ans = 1, 1
        down, d_ans = 1, 1
        for i in range(1, len(nums)):
            
            curr = nums[i]
            print("prev: ", prev, "curr: ", curr, "down: ", down)
            if prev < curr: 
                up += 1
            elif up != 1 and prev >= curr:
                u_ans = max(u_ans, up)
                up = 1
            
            if prev > curr:
                down += 1
            elif down != 1 and prev <= curr:
                d_ans = max(d_ans, down)
                down = 1
            prev = curr


        return max(max(u_ans, up), max(d_ans, down))
        