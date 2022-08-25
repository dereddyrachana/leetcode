class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        d = ["1","2","3","4","5","6","7","8","9"]
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in range(len(d)):
                            if isValid(i,j,d[c]):
                                board[i][j] = d[c]
                                if solve(board) == True:
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True
        
        def isValid(row,col,c):
            for i in range(9):
                if board[i][col] == c:
                    return False
                if board[row][i] == c:
                    return False
                idx = 3*(row//3)+(i//3)
                idy = 3*(col//3)+(i%3)
                if board[idx][idy] == c:
                    return False
            return True
        
        solve(board)
            
        
        
        
        
#         def isValid(row,col,c):
#             for i in range(9):
#                 if board[i][col]==c:
#                     return False
                
#                 if board[row][i]==c:
#                     return False
                
#                 if board[3*(row//3)+(i//3)][3*(col//3)+(i%3)]==c:
#                     return False
#             return True
#         solve(board)
        