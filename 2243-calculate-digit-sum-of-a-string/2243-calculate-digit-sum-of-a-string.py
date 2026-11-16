class Solution:
    def digitSum(self, s: str, k: int) -> str:
        string = s 
        while len(string) > k:
            tempstr = ""

            for i in range(0,len(string),k):
                temp = 0
                # print(s[i:i+k])
                for char in string[i:i+k]:
                    temp += int(char)

                tempstr += str(temp)
                # print(tempstr)
            
            string = tempstr
            # print(string)
        return string
            

        