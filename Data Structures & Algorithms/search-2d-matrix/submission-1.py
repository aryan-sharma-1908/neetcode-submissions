class Solution:
        def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            start = 0
            m = len(matrix)
            n = len(matrix[0])
            end = m * n - 1
            while start <= end:
                midIndex = int(start + (end - start) / 2)
                mrow = int(midIndex / n)
                mcol = (midIndex % n)
                if (matrix[mrow][mcol] == target):
                    return True
                elif (matrix[mrow][mcol] < target):
                    start = midIndex + 1
                else:
                    end = midIndex - 1
            return False
