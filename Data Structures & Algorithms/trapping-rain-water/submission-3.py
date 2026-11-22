class Solution:
     def trap(self, height: List[int]) -> int:
        # idea: to calculate how much water we can store above each index
        suffix_height = [height[-1]] * len(height)

        for i in range(len(height)-2,-1,-1):
            suffix_height[i] = max(suffix_height[i+1],height[i])
        prefix_height = height[0]
        stored_water = 0
        for i in range(len(height)):
            prefix_height = max(height[i],prefix_height)
            if prefix_height > height[i] and height[i] < suffix_height[i]:
                stored_water += min(prefix_height,suffix_height[i]) - height[i]

        return stored_water