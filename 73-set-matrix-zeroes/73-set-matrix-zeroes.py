class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == 0):
                    row.add(i)
                    col.add(j)
        #print(row,col)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if(i in row):
                    matrix[i][j] = 0
                    #print("row",i,j)
                    #print(matrix)
                if(j in col):
                    matrix[i][j] = 0
                    #print("col",i,j)
                    #print(matrix)
                    
        
        
        
        
        
        