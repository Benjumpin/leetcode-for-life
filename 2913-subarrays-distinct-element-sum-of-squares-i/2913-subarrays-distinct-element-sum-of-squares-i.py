class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        tsum = 0
        for i in range(len(nums)):
            # i iterated the diff array sizes 
            window_size = i + 1
            print(window_size)
            for j in range(i, len(nums)):
                tsum += len(set(nums[i : j + 1])) ** 2

        return tsum