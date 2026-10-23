class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1

        for i, val in enumerate(nums):
            if i != val:
                # val not in sorted pos
                if k == -1:
                    k = val
                else:
                    k &= val

        if k == -1:
            return 0

        return k