class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, h, changeMade = 0, len(s) - 1, False
        while l <= h:
            if s[l] != s[h]:
                s1 = s[:l] + s[l+1:]
                s2 = s[:h] + s[h+1:]
                if(s1 == s1[::-1] or s2 == s2[::-1]):
                    return True
                else:
                    return False            
            l += 1
            h -= 1
        return True