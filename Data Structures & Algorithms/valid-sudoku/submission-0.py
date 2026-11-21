class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m,n = len(board), len(board[0])
        block = [set() for _ in range(9)]
        for row in range(m):
            for col in range(n):
                if board[row][col] == '.':
                    continue
                index = row//3 * 3 + col//3
                if board[row][col] in block[index]:
                    return False
                block[index].add(board[row][col])
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == '.':
                    continue
                # check duplicate is in the row
                for i in range(m):
                    if i != row and board[i][col] == board[row][col]:
                        return False
                # check duplicate is in the col
                for j in range(n):
                    if j != col and board[row][j] == board[row][col]:
                        return False
        return True


