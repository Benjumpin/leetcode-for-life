# try again with sliding window method
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0 
        n = len(nums)
        for i in range(n):
            prod = nums[i]
            gcd_val = nums[i]
            lcm_val = nums[i]
            for j in range(i + 1, n):
                prod *= nums[j]
                gcd_val = gcd(gcd_val, nums[j])
                lcm_val = lcm(lcm_val, nums[j])
                if prod > gcd_val * lcm_val:
                    break
                if prod == gcd_val * lcm_val:
                    ans = max(ans, j - i +1)

        return ans