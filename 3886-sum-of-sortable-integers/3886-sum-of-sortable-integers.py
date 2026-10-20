import math
class Solution:
    # KMP helper func 
    def kmp(self, block, target):
        k = len(target)
        double_block = block + block

        # Build the LPS array for target
        lps = [0] * k
        prefix_length = 0
        i = 1

        while i < k:
            if target[i] == target[prefix_length]:
                prefix_length += 1
                lps[i] = prefix_length
                i += 1

            elif prefix_length > 0:
                prefix_length = lps[prefix_length - 1]

            else:
                i += 1

        # Search for target inside double_block
        i = 0
        j = 0

        while i < len(double_block):
            if double_block[i] == target[j]:
                i += 1
                j += 1

                if j == k:
                    return True

            elif j > 0:
                j = lps[j - 1]

            else:
                i += 1

        return False



    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []
        ans = 0

        # Produce all divisors of n (n inclusive) 
        for i in range(1, math.ceil(math.sqrt(n))):
            if n % i == 0:
                divisors.append(i)
                divisors.append(int(n/i))
        if n % math.sqrt(n) == 0:
            divisors.append(int(math.sqrt(n)))
        divisors.sort()

        # trivial case 
        if n == 1:
            return 1
        
        s = sorted(nums)

        for k in divisors:
            sortable = True 

            for i in range(0, n, k):
                block = nums[i:i+k]
                target = s[i:i+k]

                # Using KMP to speed up subarray check
                if not self.kmp(block, target):
                    sortable = False
                    break

                # # if slices do not have same variables, divisor  
                # # is not sortable, move on to next divisor
                # # Unecessary when using KMP
                # if sorted(block) == sorted(target):
                #     found = False
                    
                    # TOO SLOW
                    # double_block = block + block
                    # for j in range(len(block) + 1):
                    #     if double_block[j: j + k] == target:
                    #         # print("found: ", double_block[j: j + k])
                    #         found = True
                    #         break

                    # Still TOO SLOW
                    # double_block = tuple(block + block)
                    # target_tuple = tuple(target)
                    # for j in range(k):
                    #     current_rotation = double_block[j:j+k]
                    #     if current_rotation == target_tuple:
                    #         found = True
                    #         break
                    # if not found:
                    #     sortable = False
                    #     break
                    
                # else:
                #     sortable = False
                #     break

            if sortable:
                ans += k

        return ans
