# brute force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        index = deque()
        for i,nextTemp in enumerate(temperatures):
            while(len(index) != 0 and temperatures[index[-1]] < nextTemp):
                result[index[-1]] = i - index[-1]
                index.pop()
            index.append(i)

        return result