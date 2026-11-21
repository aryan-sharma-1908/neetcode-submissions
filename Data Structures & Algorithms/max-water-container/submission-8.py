class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_water,l,r = 0,0,n-1

        while l < r:
            max_water = max((r - l) * min(heights[l],heights[r]),max_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water

