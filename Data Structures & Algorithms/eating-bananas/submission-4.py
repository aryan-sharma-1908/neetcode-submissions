import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validSpeed(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours

        start,end = 1,max(piles)
        while start < end:
            mid = start + (end - start)//2
            if validSpeed(mid) <= h:
                end = mid
            else:
                start = mid + 1
        return start

        




        