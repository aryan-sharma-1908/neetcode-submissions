class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l,r):
            while l <= r:
                if(s[l] != s[r]):
                    return False
                l += 1
                r -= 1
            return True

        l, h = 0, len(s) - 1
        while l <= h:
            if s[l] != s[h]:
                return isPalindrome(l+1,h) or isPalindrome(l,h-1)
            l += 1
            h -= 1
        return True
