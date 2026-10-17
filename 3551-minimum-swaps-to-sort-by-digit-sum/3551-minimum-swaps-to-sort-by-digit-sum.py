import copy
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        dsum = [0 for _ in range(len(nums))]
        pair = []

        for i in range(len(nums)):
            num = nums[i]
            for digit in list(str(num)):
                dsum[i] += int(digit)
            pair.append((dsum[i], num))

        target = sorted(pair)
        val_to_target_idx = {}

        for i in range(len(target)):
            digit = target[i][1]
            val_to_target_idx[digit] = i
        
        print(val_to_target_idx)

        visited = [False] * len(nums)
        swaps = 0
        
        for i in range(len(nums)):
            if visited[i] or pair[i] == target[i]: 
                # visited or in right pos then skip
                continue 

            cycle = 0
            temp = i
            while not visited[temp]:
                visited[temp] = True
                # find where element belongs in target arr
                temp = val_to_target_idx[pair[temp][1]]
                cycle += 1

            if cycle > 1:
                swaps += cycle - 1 

        return swaps 