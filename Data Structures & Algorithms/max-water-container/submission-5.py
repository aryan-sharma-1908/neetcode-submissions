class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i, height in enumerate(heights):
            for j in range(i + 1, len(heights)):
                minHeight = min([height,heights[j]])
                maxArea = max(maxArea,minHeight * (j - i))
        return maxArea