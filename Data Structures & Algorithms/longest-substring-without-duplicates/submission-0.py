class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            nonRepeating = True
            seen = defaultdict(int)
            for j in range(i, len(s)):
                if(not s[j] in seen and nonRepeating):
                    maxLen = max(maxLen, j - i + 1)
                    seen[s[j]] = 1
                else:
                    nonRepeating = False
                    seen[s[j]] += 1

        return maxLen
        