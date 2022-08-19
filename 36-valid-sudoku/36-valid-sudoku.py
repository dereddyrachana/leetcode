class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {x:[] for x in range(9)}
        col = {x:[] for x in range(9)}
        box = {x:[] for x in range(9)}
        for i in range(0,9):
            for j in range(0,9):
                val = board[i][j]
                print('Val',val)
                if val == '.':
                    continue
                else:
                    if(val not in row[i]):
                        row[i].append(val)
                        print(row)
                    else:
                        return False
                    if(val not in col[j]):
                        col[j].append(val)
                        print(col)
                    else:
                        return False
                    idx = (i//3) * 3 + (j//3) 
                    if(val not in box[idx]):
                        box[idx].append(val)
                    else:
                        return False
        return True
               
        
                    

                    