class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in row:
                    row.add(board[i][j])
                else:
                    return False

        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in col:
                    col.add(board[i][j])
                else:
                    return False   
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True

                