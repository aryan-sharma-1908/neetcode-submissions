class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        block = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        for row in range(n):
            for col in range(n):
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


