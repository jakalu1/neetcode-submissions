class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # each value is auto initialized to an empty set
        rows = collections.defaultdict(set) #key:value pair = row #:set of values in that row
        squares = collections.defaultdict(set) #key:value pair = (subgrid row, col):set of values in that subgrid
                                                                # remember subgrid row and col are gained by doing row//3 and col//3

        #iterate over each value in the board. so row 0, col 0, col 1, col 2, etc
                                            #  then row 1, col 0, col 1, col 2, etc
        for curr_row in range(len(board)):
            for curr_col in range(len(board)):
                #check if its empty ".", if it is, then just skip that iteration with continue
                if board[curr_row][curr_col] == ".":
                    continue
                
                if (board[curr_row][curr_col] in rows[curr_row] or 
                    board[curr_row][curr_col] in cols[curr_col] or
                    board[curr_row][curr_col] in squares[(curr_row//3, curr_col//3)]):
                    return False
                else:
                    cols[curr_col].add(board[curr_row][curr_col])
                    rows[curr_row].add(board[curr_row][curr_col])
                    squares[(curr_row//3, curr_col//3)].add(board[curr_row][curr_col])
            
        return True