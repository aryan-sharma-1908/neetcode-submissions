import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        while s <= e:
            m = int(s + (e - s)/2)
            hrs = self.hoursToEat(m, piles)
            if(hrs > h):
                s = m + 1
            else:
                e = m - 1
        return s

    def hoursToEat(self, k : int, piles: List[int]) -> int:
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile / k)
        return hrs