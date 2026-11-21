class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(tuple(s)) == sorted(tuple(t))