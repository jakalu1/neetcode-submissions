class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check each row, make a different set seen, then check if there are duplicates
        #if not, move on to next row 
        #the inner loop is iterating one column to the right by the way!
        for row in range(len(board)):
            seen = set()
            for j in range(len(board[row])):
                if board[row][j] == '.':
                    continue
                elif board[row][j] in seen:
                    return False
                else:
                    seen.add(board[row][j])

        #we want the col to stay the same, but the board to iterate DOWN one row
        for col in range(len(board)):
            seen = set()
            for j in range(len(board[col])):
                if board[j][col] == '.':
                    continue 
                elif board[j][col] in seen:
                    return False
                else:
                    seen.add(board[j][col])

        for square in range(9):
            seen = set()

            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    
                    if board[row][col] == '.':
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])

        return True            