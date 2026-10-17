import copy
class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        pair = []
        for num in nums:
            d_sum = sum(int(digit) for digit in str(num))
            pair.append((d_sum, num))

        target = sorted(pair)

        val_to_target_idx = {val: i for i, (d_sum, val) in enumerate(target)}
        
        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or pair[i] == target[i]:
                continue

            cycle_length = 0
            curr = i

            while not visited[curr]:
                visited[curr] = True

                curr = val_to_target_idx[pair[curr][1]]
                cycle_length += 1

            if cycle_length > 1:
                swaps += (cycle_length - 1)
        
        return swaps