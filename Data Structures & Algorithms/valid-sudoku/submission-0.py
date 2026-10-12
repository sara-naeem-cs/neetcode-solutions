class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_hash = {}
        quad_hash = {}

        for k in range(9):
            col_hash[k] = set()
            quad_hash[k] = set()

        for i in range(9):
            temp_set = set() #define empty set

            for j in range(9):
                if board[i][j] != ".":
                    #See if number is in temp set
                    if board[i][j] in temp_set:
                        return False
                    else:
                        #Else add to temp set
                        temp_set.add(board[i][j])
                    
                    #See if number is in col_hash[j]
                    if board[i][j] in col_hash[j]:
                        return False
                    else:
                        col_hash[j].add(board[i][j])

                    #Calculate quadrant
                    quadrant = (i//3)*3+(j//3)

                    #See if number is in quad_hash[calculated_val]
                    if board[i][j] in quad_hash[quadrant]:
                        return False
                    else:
                        quad_hash[quadrant].add(board[i][j])

            temp_set = set()
        return True

        