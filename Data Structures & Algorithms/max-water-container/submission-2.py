class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        maxArea = 0
        for i, Hti in enumerate(heights):
            for j in range(i+1,len(heights)):
                bar_distance = j - i
                min_height_in_bar_pair = Hti if Hti < heights[j] else heights[j]
                maxArea = max(maxArea,bar_distance * min_height_in_bar_pair)


        return maxArea