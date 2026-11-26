class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n,max_area = len(heights),0
        st = []
        pse = [-1] * n
        nse = [len(heights)] * n
        for i in range(len(heights)):
            while len(st) > 0 and heights[st[-1]] > heights[i]:
                nse[st.pop()] = i
            st.append(i)
        st = []
        for i in range(len(heights)-1,-1,-1):
            while len(st) > 0 and heights[st[-1]] > heights[i]:
                pse[st.pop()] = i
            st.append(i)


        for i in range(len(heights)):
            area = (i - pse[i]) * heights[i] + (nse[i] - i) * heights[i] - heights[i]
            max_area = max(area,max_area)

        return max_area
                    


        
        