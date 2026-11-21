class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indicesMap = {}
        maxLen = 0
        l,r = 0,0
        while r < len(s):
            if s[r] in indicesMap:
                while s[l] != s[r]:
                    del indicesMap[s[l]]
                    l += 1
                l += 1
            indicesMap[s[r]] = r
            maxLen = max(maxLen,r - l + 1)
            r += 1
        return maxLen
            