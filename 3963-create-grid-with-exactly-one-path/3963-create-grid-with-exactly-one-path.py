class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = []
        row1, rown = "", ""
        for c in range(n):
            row1 += "."
            if c != 0:
                rown += "#"
        ans.append(row1)

        for r in range(m-1):
            ans.append(rown + ".")
        
    
        return ans 


