class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_begin = 0
        col_begin = 0
        row_end = len(matrix) - 1
        col_end = len(matrix[0]) - 1
        ans = []
        while(row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin,col_end+1):
                # print(matrix[row_begin][i])
                ans.append(matrix[row_begin][i])
            row_begin+=1
            for j in range(row_begin,row_end+1):
                ans.append(matrix[j][col_end])
                # print(matrix[j][col_end])
            col_end-=1
            if(row_begin <= row_end):
                for i in range(col_end, col_begin-1,-1):
                    # print(matrix[row_end][i])
                    ans.append(matrix[row_end][i])
                row_end-=1
            if(col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    # print(matrix[i][col_begin])
                    ans.append(matrix[i][col_begin])
                col_begin+=1
        return ans
            

        
            
            