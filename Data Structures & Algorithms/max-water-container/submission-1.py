class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #goal: find two elements:
        # 1: smaller than x and is farthest away from the x
        # 2: bigger or equal to x and is farthest away from the x (we can move x upon finding this no need to search further or find option 1)
        maxArea = 0
        for i, x in enumerate(heights):
            j = len(heights) - 1
            while(i < j and heights[j] < x):
                smaller_and_farthest = False
                if(heights[j] < x and not smaller_and_farthest):
                    smaller_and_farthest = True
                    maxArea = max(maxArea,heights[j] * (j - i))
                j -= 1
            if(j > i):
                if(heights[j] >= x):
                    maxArea = max(maxArea,x * (j - i))


        return maxArea