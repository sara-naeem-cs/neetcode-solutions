class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLUMNS = len(board[0])
        path = set()


        def dfs(r, c, i):
            if i==len(word):
                return True
            
            #When to return false
            #1. out of bounds
            #2. the letter is not equal to this given (r,c) position
            #3. if it's already in the set

            if (r < 0 or c < 0 or r>=ROWS or c>=COLUMNS 
            or (r,c) in path or board[r][c]!= word[i]):
                return False
            
            #We found the character we wanted so add it to the path:
            path.add((r,c))

            #Call dfs on adjacent positions
            res = (dfs(r-1, c, i+1) or
            dfs(r+1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1))

            #we tried this cell, we remove it so that it is
            # available to try again in future attempts
            path.remove((r,c))
            return res

        for i in range(ROWS):
            for j in range(COLUMNS):
                if dfs(i,j, 0):
                    return True
        
        return False




        