class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        columns = set()
        rows = set()


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    #Add this row and column to our sets
                    columns.add(j)
                    rows.add(i)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in columns:
                    matrix[i][j] = 0









"""
                    #Set column to zeroes if it haven't already
                    if j not in columns:
                        columns.add(j)
                        #Set column to zeros
                        for row in range(len(matrix)):
                            matrix[row][j] = 0
                        
                    #Set row to zeroes if we haven't already
                    if i not in rows:
                        rows.add(i)
                        for col in range(len(matrix[0])):
                            matrix[i][col] = 0
"""

