class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prevPosition = -1
        for ch1 in s:
            eleFound = False
            for j, ch2 in enumerate(t):
                if(ch1 == ch2 and j > prevPosition):
                    prevPosition = j
                    eleFound = True
                    break
            if(not eleFound):
                return False
            
        return True
