class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #
        # for row in matrix:
        #     row.reverse()
#         n = len(matrix)
#         for row in range(n):
#             for col in range(row):
#                 matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
#         for row in matrix:
#             row.reverse()
            