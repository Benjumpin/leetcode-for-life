class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller, dup = 0, 0
        ans = []
        for i in nums:
            if i < target:
                smaller += 1
            elif i == target:
                dup += 1

        for i in range(smaller, smaller + dup):
            ans.append(i)

        return ans