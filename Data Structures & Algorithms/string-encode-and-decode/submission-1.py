class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        lengthOfString = 0
        i = 0
        lenInChar = ""
        while(i < len(s)):
            j = i
            while(j < len(s) and s[j] != '#' ):
                j += 1
            if j >= len(s):
                break
            lengthOfString = int(s[i:j])
            i = j + 1
            decoded.append(s[ i : i + lengthOfString ])
            i += lengthOfString
        return decoded
            
            
            