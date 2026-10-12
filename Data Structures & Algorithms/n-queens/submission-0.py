class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # keep track of 
        # Columns
        # Negative Diagonal (going down along diagonal) --> (r-c) is 0
        # Positive Diagonal (going up along diagonal) --> (r+c) is constant (i.e. len(n))

        #We can't palce queen in the same column, negative diagonal or the posititve diagonal

        colSet = set()
        negDiag = set() #(r+c)
        posDiag = set() #(r-c)

        res = []
        board = [["."]*n for i in range(n)]

        def dfs(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)

            #didn't reach base case:
            #Try all positions we can place a queen in

            for col in range(n):
                if col in colSet or (row+col) in posDiag or (row-col) in negDiag:
                    continue
                
                #We can use this r,c pair
                #Update sets
                colSet.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)

                #Update board
                board[row][col] = "Q"

                dfs(row+1)

                #Clean everything for next iteration
                colSet.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)

                board[row][col] = "."
        
        dfs(0)

        return res 


            

