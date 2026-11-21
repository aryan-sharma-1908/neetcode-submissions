class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if len(blocks) == 1 and blocks[0] == 'W':
            return 1

        l,r,recolors, minRecolors = 0,0,0,0

        while r  < k:
            if blocks[r] == 'W':
                recolors += 1
            r += 1
        minRecolors = recolors

        while r < len(blocks):
            if blocks[l] == 'W':
                recolors -= 1
            if blocks[r] == 'W':
                recolors += 1
            minRecolors = min(minRecolors, recolors)
            l += 1
            r += 1
        
        return minRecolors
        
        