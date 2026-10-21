class Solution:
    def minOperations(self, s: str) -> int:
        if s == "".join(sorted(s)):
            return 0
        elif s[0] == min(s) or s[-1] == max(s):
            return 1
        elif len(s) == 2:
            return -1
        elif min(s) in s[:-1] or max(s) in s[1:]:
            return 2
        else:
            return 3
        
        