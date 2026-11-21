class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        block = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                index = row//3 * 3 + col//3
                if board[row][col] in block[index]:
                    return False
                block[index].add(board[row][col])
                if board[row][col] in rows[col]:
                    return False
                rows[col].add(board[row][col])
                if board[row][col] in cols[row]:
                    return False
                cols[row].add(board[row][col])
        return True


