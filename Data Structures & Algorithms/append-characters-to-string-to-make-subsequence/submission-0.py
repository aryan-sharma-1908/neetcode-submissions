class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        positionToSearch = 0
        for i,ch1 in enumerate(t):
            eleFound = False
            for j in range(positionToSearch, len(s)):
                if(ch1 == s[j]):
                    positionToSearch = j + 1
                    eleFound = True
                    break
                
            if(not eleFound):
                return len(t) - i

        return 0