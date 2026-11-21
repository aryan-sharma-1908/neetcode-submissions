class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i1,i2 = 0,0
        while i1 < len(t) and i2 < len(s):
            if(t[i1] == s[i2]):
                i1 += 1
                i2 += 1
            else:
                i2 += 1
        
        return len(t) - i1