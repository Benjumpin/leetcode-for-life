class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        aam, aad = arriveAlice.split("-")
        lam, lad = leaveAlice.split("-")
        abm, abd = arriveBob.split("-")
        lbm, lbd = leaveBob.split("-")

        tdays = 0
        
        
        for i in range(len(days)):
            tdays += days[i]
            
            if i == int(aam) - 1:
                arriveAlice = tdays + int(aad) - days[i]
            if i == int(lam) - 1:
                leaveAlice = tdays + int(lad) - days[i]
            if i == int(abm) - 1:
                arriveBob = tdays + int(abd) - days[i]
            if i == int(lbm) - 1:
                leaveBob = tdays + int(lbd) - days[i]

        overlap_start = max(arriveAlice, arriveBob)
        overlap_end = min(leaveAlice, leaveBob)
        
        print(arriveAlice, leaveAlice, arriveBob, leaveBob)
        print(overlap_start, overlap_end)
        
        return max(0, overlap_end - overlap_start + 1)