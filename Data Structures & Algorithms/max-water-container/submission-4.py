class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #goal: find two elements:
        #bigger or equal to x and is farthest away from the x (we can move x upon finding this no need to search further or find option 1)
        maxArea = 0
        for i, x in enumerate(heights):
            j = len(heights) - 1
            while(i < j):
                if(heights[j] >= x):
                    maxArea = max(maxArea, x * (j - i))
                    break
                maxArea = max(maxArea, heights[j] * (j - i))
                j -= 1

        return maxArea