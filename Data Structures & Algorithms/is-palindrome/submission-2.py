class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        listOfChar = []
        for ch in s:
            if (ch.isalnum()):
                listOfChar.append(ch)
        for i in range(0, len(listOfChar) // 2):
            if (listOfChar[i] != listOfChar[len(listOfChar) - i - 1]):
                return False
        return True
