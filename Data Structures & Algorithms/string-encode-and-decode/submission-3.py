class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(s)
            encoded.append("$#split#$")
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        decoded = []
        decoded = s.split("$#split#$")
        del decoded[-1]
        return decoded

            
            
            