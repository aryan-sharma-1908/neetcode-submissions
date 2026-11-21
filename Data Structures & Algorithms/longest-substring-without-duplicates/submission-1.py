class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l,r = 0,0
        seen = defaultdict(int)
        while r < len(s):
            while seen[s[r]] >= 1:
                seen[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            seen[s[r]] += 1
            r += 1
        return maxLen
            

        