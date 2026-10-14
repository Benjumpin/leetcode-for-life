class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = ""
        a = 9
        temp = 0
        if (num * 9) < sum: 
            return ""

        for i in range(num):
            while a >= 0:
                if temp + a <= sum: 
                    ans += str(a)
                    temp += a
                    break
                else:
                    a -= 1
            # print(ans)
        return ans





    # naive approach TLE
    # def maxSumOfSquares(self, num: int, sum: int) -> str:
    #     max = ""
    #     if (num * 9) < sum: 
    #         return ""

    #     for i in range(num):
    #         max += "9"

    #     while True:
    #         temp = 0
    #         for c in max:
    #             temp += int(c)
    #         # print(temp)
    #         if temp == sum:
    #             return max
    #         else:
    #             max = str(int(max)-1)

            
           

        