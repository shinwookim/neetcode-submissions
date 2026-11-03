class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Rows/Cols
        for row in range(9):
            seen_in_row = set()
            seen_in_col = set()
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in seen_in_row:
                        return False
                    else:
                        seen_in_row.add(board[row][col])
                if board[col][row] != ".":
                    if board[col][row] in seen_in_col:
                        return False
                    else:
                        seen_in_col.add(board[col][row])
        for sqRow in range(3):
            for sqCol in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[3 * sqRow + i][3 * sqCol + j] != ".":
                            if board[3 * sqRow + i][3 * sqCol + j] in seen:
                                return False
                            else:
                                seen.add(board[3 * sqRow + i][3 * sqCol + j])
        return True
