import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_eating_rate, max_eating_rate = 1, max(piles)
        ans = 1

        while min_eating_rate <= max_eating_rate:
            mid = min_eating_rate + (max_eating_rate - min_eating_rate)//2
            if(self.can_finish_under_time_limit(mid,piles,h)):
                ans = mid
                max_eating_rate = mid - 1
            else:
                min_eating_rate = mid + 1

        return ans

    def can_finish_under_time_limit(self, speed, piles, h):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / speed)
        
        return True if total_hours <= h else False